<template>
  <div class="dashboard">
    <div class="flex flex-row place-content-center content-center">
      <button
        @click="redirectCreateNewSet"
        class="w-full text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-md px-5 py-2.5 mb-4 mx-2 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800 poppins-font"
      >
        CREATE A NEW SET
      </button>
      <button
        @click="redirectViewAllSets"
        class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-md px-5 py-2.5 mb-4 mx-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 poppins-font"
      >
        VIEW ALL SETS
      </button>
    </div>
    <h1 class="text-white">Dashboard {{ email }}</h1>
    <h1 class="text-white">User ID: {{ user_id }}</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DashboardView",
  data() {
    return {
      email: "",
      user_id: "-1",
    };
  },
  methods: {
    async fetchData() {
      const { data } = await axios.post("http://localhost:5000/get_data", {
        email: this.email,
      });
      this.user_id = data;
    },
    async fetchSets() {
      const { data } = await axios.post("http://localhost:5000/get_sets", {
        id: this.user_id,
      });
      console.log(data);
    },
    redirectCreateNewSet() {
      this.$store.commit('setUserID', this.user_id);
      this.$router.push("create");
    },
    redirectViewAllSets() {
      this.$router.push('show-all')
    }
  },
  components: {},
  async created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
      this.$store.commit("setCurrentUser", localStorage.email);
    }
    await this.fetchData();
  },
  watch: {
    user_id: function (newUserId, oldUserId) {
      if (newUserId != oldUserId) {
        console.log(`New User ID: ${newUserId}`);
        console.log(`Previous User ID: ${oldUserId}`);
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}
</style>
