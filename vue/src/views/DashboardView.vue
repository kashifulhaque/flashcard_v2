<template>
  <div class="dashboard">
    <p class="text-gray-400 text-xl font-medium px-4" v-if="user_id != ''">User ID: <span class="text-xl text-white">{{ user_id }}</span></p>
    <p class="text-gray-400 text-xl font-medium px-4">
      Username: <span class="text-white text-3xl">{{ email.substring(0, email.indexOf('@')) }}</span>
    </p>
    <p class="text-gray-400 text-xl font-medium px-4">
      Email ID: <span class="text-white text-3xl">{{ email }}</span>
    </p>
    <div class="flex flex-row place-content-center content-center mt-4">
      <button
        @click="redirectCreateNewSet"
        class="w-1/3 text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-md px-6 py-3 mb-4 mx-2 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800 poppins-font"
      >
        CREATE A NEW SET
      </button>
      <button
        @click="redirectViewAllSets"
        class="w-1/3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-md px-6 py-3 mb-4 mx-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 poppins-font"
      >
        VIEW ALL SETS
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DashboardView",
  data() {
    return {
      email: '',
      user_id: '',
      login_timestamp: ''
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
      this.$store.commit("setUserID", this.user_id);
      this.$router.push("create");
    },
    redirectViewAllSets() {
      this.$router.push("show-all");
    },
  },
  components: {},
  async created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
      this.$store.commit("setCurrentUser", localStorage.email);
    }
    const d = new Date();
    this.login_timestamp = d.getTime();

    await this.fetchData();
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}
</style>
