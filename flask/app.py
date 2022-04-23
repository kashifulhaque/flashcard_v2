from importlib.metadata import requires
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)
CORS(app)
current_dir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "testdb_modified.sqlite3")
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "another.sqlite3")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "another2.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

class Sets(db.Model):
    __tablename__ = 'sets'
    set_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

class Cards(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_id = db.Column(db.Integer, db.ForeignKey("sets.set_id"))

class Sides(db.Model):
    __tablename__ = 'sides'
    side_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_id = db.Column(db.Integer, db.ForeignKey("cards.card_id"))
    content = db.Column(db.String, nullable=False)
    side_order = db.Column(db.Integer, nullable=False)

accounts = [
    {
        'email': 'someone@example.com',
        'password': 'password'
    },
    {
        'email': 'haque.k@outlook.com',
        'password': 'password'
    },
]

@app.route('/login', methods=['POST'])
def login():
    record = json.loads(request.data)
    email = record['email']
    password = record['password']
    
    user = Users.query.filter_by(email=email).first()
    if user:
        # If a user exists with the given email, check it's password hash
        if check_password_hash(user.password, password):
            # Correct password, logged in
            return 'Login success', 200
        else:
            return 'Incorrect password', 401
    else:
        return 'Not registered', 401

@app.route('/register', methods=['POST'])
def register():
    record = json.loads(request.data)
    email = record['email']
    password = record['password']

    # Check if the email exists in the database
    user = Users.query.filter_by(email=email).first()
    if not user:
        # Hash the password
        hashed_pw = generate_password_hash(password, method='sha256')
        new_user = Users(email=email, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        return 'Registered', 200
    else:
        # There exists a user with the given email
        # Handle appropriately
        return 'Failed', 401

@app.route('/get_data', methods=['POST'])
def get_data():
    record = json.loads(request.data)
    email = record['email']

    user = Users.query.filter_by(email=email).first()
    return str(user.user_id), 200

@app.route('/save_set', methods=['POST'])
def save_set():
    record = json.loads(request.data)
    setname = record['setname']
    data = record['data']
    user_email = record['user_email']
    
    user = Users.query.filter_by(email=user_email).first()

    all_sets = len(Sets.query.all()) * 2

    new_set = Sets(set_id=all_sets, name=setname, user_id=user.user_id)
    # new_set = Sets(name=setname, user_id=user.user_id)

    db.session.add(new_set)
    db.session.commit()
    
    cards = []
    card_ids = []
    for d in data:
        all_cards = len(Cards.query.all()) * 2
        new_card = Cards(card_id=all_cards, set_id=new_set.set_id)
        cards.append(d)
        card_ids.append(all_cards)

        db.session.add(new_card)
    db.session.commit()
    
    i = 0
    for card in cards:
        sideA_text = card['cardA']
        sideB_text = card['cardB']
        
        all_sides = len(Sides.query.all()) + 1
        new_sideA = Sides(side_id=all_sides, card_id=card_ids[i], content=sideA_text, side_order=0)
        all_sides += 1
        new_sideB = Sides(side_id=all_sides, card_id=card_ids[i], content=sideB_text, side_order=1)

        db.session.add(new_sideA)
        db.session.commit()
        db.session.add(new_sideB)
        db.session.commit()
        i += 1

    return 'done', 200

@app.route('/fetch_sets', methods=['POST'])
def fetch_sets():
    record = json.loads(request.data)
    email = record['email']

    user = Users.query.filter_by(email=email).first()
    sets = Sets.query.filter_by(user_id=user.user_id)

    data = {}
    set_names = {}
    set_cards = {}
    all_cards = {}

    for set in sets:
        set_names[set.set_id] = set.name
        cards = Cards.query.filter_by(set_id=set.set_id)
        set_cards[set.set_id] = []

        for card in cards:
            card_with_sides = {}
            set_cards[set.set_id].append(card.card_id)
            sides = Sides.query.filter_by(card_id=card.card_id)

            for side in sides:
                card_with_sides[side.side_order] = side.content
            
            all_cards[card.card_id] = card_with_sides
    
    data['set_names'] = set_names
    data['set_cards'] = set_cards
    data['cards'] = all_cards
    json_obj = json.dumps(data, indent=4)
    return jsonify(json_obj);

@app.route('/delete_set', methods=['POST'])
def delete_set():
    record = json.loads(request.data)
    email = record['email']
    set_id_to_delete = int(record['set_id'])
    print(f'ID to delete: {type(set_id_to_delete)}')
    
    user = Users.query.filter_by(email=email).first()
    sets = Sets.query.filter_by(user_id=user.user_id)

    found = False
    for set in sets:
        print(set.set_id)
        if set_id_to_delete == set.set_id:
            found = True
            Sets.query.filter_by(set_id=set.set_id).delete()
            cards = Cards.query.filter_by(set_id=set_id_to_delete)

            for card in cards:
                Cards.query.filter_by(set_id=set_id_to_delete).delete()

    if found:
        db.session.commit()
        return 'Delete', 200
    if not found:
        return 'Set does not exist', 200
