<template>
  <nav class="bg-gray-800 mb-4">
    <div class="mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex-shrink-0 flex items-center">
            <router-link to="/">
              <i class="fa-solid fa-bolt text-white"></i><i class="fa-solid fa-address-card text-white ml-1"></i>
              <span class="ml-2 nunito-font text-white text-2xl">Flashcards</span>
            </router-link>
          </div>
          <div class="hidden sm:block sm:ml-2">
            <div class="flex space-x-4">
              <button @click="logout" v-if="$route.name != 'home'" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Logout</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {
    }
  },
  methods: {
    logout() {
      if(localStorage.email) {
        localStorage.clear();
        this.$router.push('/');
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600&display=swap');

.nunito-font {
  font-family: 'Nunito', sans-serif;
}
</style>
