import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    showLogout: false,
    userEmail: "",
    userID: -1,
    setTitle: "",
    setID: "",
    cardIDs: [],
    allSides: [],
  },
  getters: {},
  mutations: {
    changeLogout(state) {
      state.showLogout = !state.showLogout;
    },
    setCurrentUser(state, email) {
      state.userEmail = email;
    },
    setUserID(state, id) {
      state.userID = id;
    },
    changeSetTitle(state, title) {
      state.setTitle = title;
    },
    changeSetID(state, id) {
      state.setID = id;
    },
    changeCardID(state, id) {
      state.cardIDs = id;
    },
    changeAllSides(state, sides) {
      state.allSides = sides;
    }
  },
  actions: {},
  modules: {},
});
