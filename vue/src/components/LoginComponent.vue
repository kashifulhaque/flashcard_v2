<template>
  <div :class="{ shake: animate }">
    <div
      class="p-4 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md sm:p-6 lg:p-8 dark:bg-gray-900 dark:border-gray-700"
    >
      <form class="space-y-6" action="#">
        <h5 class="text-3xl font-bold text-gray-900 dark:text-white">Login</h5>
        <div>
          <label
            for="email"
            class="block mb-2 text-md font-medium text-gray-900 dark:text-gray-300"
            >Enter email</label
          >
          <input
            type="email"
            name="email"
            id="email"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="someone@example.com"
            required
            v-model="email"
          />
        </div>
        <div>
          <label
            for="password"
            class="block mb-2 text-md font-medium text-gray-900 dark:text-gray-300"
            >Enter password</label
          >
          <input
            type="password"
            name="password"
            id="password"
            placeholder="••••••••"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            required
            v-model="password"
          />
        </div>
        <button
          type="submit"
          @click.prevent="login"
          class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-semibold rounded-lg text-md px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          LOGIN
        </button>
        <small class="text-yellow-300 italic" v-if="incorrect"
          >Incorrect email and/or password</small
        >
        <div class="text-md font-medium text-gray-500 dark:text-gray-300">
          Not registered?
          <a
            @click="changeStuff"
            class="text-blue-700 hover:underline dark:text-blue-500 cursor-pointer"
            >Create an account</a
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginComponent",
  data() {
    return {
      email: "",
      password: "",
      incorrect: false,
      animate: false,
    };
  },
  methods: {
    changeStuff() {
      this.$emit("loginState", false);
    },
    async login() {
      // Check if the user has filled in the email and password
      if (this.email && this.password) {
        try {
          const { data } = await axios.post("http://localhost:5000/login", {
            email: this.email,
            password: this.password,
          });

          if(data === 'Login success') {
            // Store the email in localStorage, to mark the user as logged in
            // Redirect the user to the dashboard
            localStorage.email = this.email;
            this.$router.push('dashboard');
          }
        } catch (e) {
          this.incorrect = true;
        }
      } else {
        // Shake the component
        this.shakeComponent();
      }
    },
    shakeComponent() {
      // Animate vue component: https://codepen.io/aut0maat10/pen/ExaNZNo
      this.animate = true;
      setTimeout(() => {
        this.animate = false;
      }, 1000);
    },
  },
  mounted() {
    // Check if the user is logged in
    // How to check? Check if the localStorage contains a key named 'email' and does it have a value?
    // If it has a value, redirect the user to the dashboard
    // This check works as a barebones route guard
    if(localStorage.email) {
      this.$router.push('dashboard');
    }
  }
};
</script>

<style scoped>
.shake {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
}

@keyframes shake {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }
  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
