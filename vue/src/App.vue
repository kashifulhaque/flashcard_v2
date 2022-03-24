<template>
  <div class="app">
    <HeaderComponent />
    <div class="container">
      <router-view />
    </div>
  </div>
  <!-- https://flowbite.com/docs/components/card/ -->
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue';

export default {
  components: {
    HeaderComponent
  }
}
</script>

<style scoped></style>
