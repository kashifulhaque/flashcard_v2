<template>
  <div :class="{ shake: animate }">
    <div
      class="p-4 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md sm:p-6 lg:p-8 dark:bg-gray-900 dark:border-gray-700"
    >
      <form class="space-y-6" action="#">
        <h5 class="text-xl font-medium text-gray-900 dark:text-white">
          Register
        </h5>
        <div>
          <label
            for="email"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Your email</label
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
          <small class="text-zinc-300 italic" v-if="invalidEmail">Invalid E-mail address</small>
          <small class="text-zinc-300 italic" v-if="emailExists">E-mail already taken</small>
        </div>
        <div>
          <label
            for="password"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Your password</label
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
          <small class="text-zinc-300 italic" v-if="passwordNoMatch">Passwords do not match</small>
        </div>
        <div>
          <label
            for="repeatpassword"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Your password again</label
          >
          <input
            type="password"
            name="repeatpassword"
            id="repeatpassword"
            placeholder="••••••••"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            required
            v-model="repeatPassword"
          />
        </div>
        <button
          type="submit"
          @click.prevent="register"
          class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Register
        </button>
        <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
          Already registered?
          <a
            @click="changeStuff"
            class="text-blue-700 hover:underline dark:text-blue-500 cursor-pointer"
            >Login here</a
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterComponent",
  data() {
    return {
      email: "",
      invalidEmail: false,
      emailExists: false,
      password: "",
      repeatPassword: "",
      passwordNoMatch: false,
      animate: false,
    };
  },
  methods: {
    changeStuff() {
      this.$emit("loginState", true);
    },
    async register() {
      if (this.email && this.password && this.repeatPassword) {
        // Check if the email is in correct format
        if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))) {
          this.shakeComponent();
          this.invalidEmail = true;
          return;
        }

        // Check if 'password' and 'repeatPassword' match
        if(this.password === this.repeatPassword) {
          // Proceed with account creation
          const userData = {
            email: this.email,
            password: this.password
          };
          try {
            const { data } = await axios.post("http://localhost:5000/register", userData);
            if(data === 'Registered') {
              this.changeStuff();
            }
          } catch(e) {
            this.emailExists = true;
          }
        } else {
          this.passwordNoMatch = true;
          this.shakeComponent();
        }
      } else {
        this.shakeComponent();
      }
    },
    shakeComponent() {
      // Animate vue component: https://codepen.io/aut0maat10/pen/ExaNZNo
        this.animate = true;
        setTimeout(() => {
          this.animate = false;
        }, 1000);
    }
  },
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
