import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    showLogout: false,
    userEmail: '',
    userID: -1
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
    }
  },
  actions: {},
  modules: {}
})
