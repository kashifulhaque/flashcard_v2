<template>
  <tr class="">
    <td>
      <input
        type="text"
        name="sideAText"
        id="sideAText"
        class="w-full p-2 rounded-lg"
        placeholder="Card side A text goes here ..."
        v-model="cardContent['cardA']"
        v-on:input="$emit('get-card-data', { 'card': 'cardA', 'cardContent': cardContent['cardA'] })"
      />
    </td>
    <td>
      <input
        type="text"
        name="sideBText"
        id="sideBText"
        class="w-full p-2 rounded-lg"
        placeholder="Card side B text goes here ..."
        v-model="cardContent['cardB']"
        v-on:input="$emit('get-card-data', { 'card': 'cardB', 'cardContent': cardContent['cardB'] })"
      />
    </td>
  </tr>
</template>

<script>
export default {
  name: "CardContentComponent",
  data() {
    return {
      cardContent: {},
    };
  },
  props: ["content"],
  mounted() {
    this.cardContent = this.$props["content"];
  },
};
</script>

<style scoped></style>
