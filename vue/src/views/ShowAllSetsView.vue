<template>
  <div class="show-all-sets">
    <p class="text-white text-3xl">All sets shall be displayed here</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ShowAllSetsView",
  data() {
    return {
      email: '',
      cards: {},
      set_cards: {},
      set_names: {},
      card_package: []
    };
  },
  methods: {},
  components: {},
  async created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
      this.$store.commit("setCurrentUser", localStorage.email);

      // Fetch current user's set of cards from the database
      const { data } = await axios.post("http://localhost:5000/fetch_sets", { email: this.email })
      const { cards, set_cards, set_names } = JSON.parse(data);
      this.cards = cards;
      this.set_cards = set_cards;
      this.set_names = set_names;

      for(const i in set_names) {
        const pkg = {};
        pkg['set_id'] = i;
        pkg['set_name'] = set_names[i];
        pkg['cards'] = [];
        pkg['sides'] = [];

        for(const j of set_cards[i]) {
          pkg['cards'] = [... set_cards[i]];
          pkg['sides'].push(cards[j]);
        }
        this.card_package.push(pkg);
      }

      console.log(this.card_package);
    }
  },
  watch: {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}
</style>
