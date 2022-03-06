<template>
  <div class="home">
    <LoginComponent v-if="showLogin" @loginState="showLogin = $event" />
    <RegisterComponent v-else @loginState="showLogin = $event" />
  </div>
</template>

<script>
import LoginComponent from '@/components/LoginComponent.vue'
import RegisterComponent from '@/components/RegisterComponent.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      showLogin: true
    }
  },
  components: {
    LoginComponent,
    RegisterComponent
  }
}
</script>
