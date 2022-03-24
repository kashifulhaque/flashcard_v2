<template>
  <div class="read">
    <h1 class="text-white text-2xl">Your card</h1>
    <p class="text-white">{{ sides }}</p>
  </div>
</template>

<script>
export default {
  name: "ReadCardComponent",
  data() {
    return {
    };
  },
  props: ['sides'],
  mounted() {
    console.log(this.$props);
  }
};
</script>

<style></style>
