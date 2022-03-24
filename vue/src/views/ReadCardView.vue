<template>
  <div class="read-card-view">
    <p class="text-white text-2xl">Title: {{ setTitle }}</p>
    <p class="text-white text-2xl">Set ID: {{ setID }}</p>
    <p class="text-white text-2xl">Sides</p>
    <ul class="ml-8 mr-8">
      <li
        style="list-style: none"
        class="text-white cursor-pointer"
        v-for="(side, i) in allSides"
        v-bind:key="i"
      >
        <CardComponent
          v-bind:idx="i + 1"
          v-bind:sidetext="side"
          v-bind:currentside="currentSides"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import CardComponent from "@/components/CardComponent.vue";

export default {
  name: "ReadCardView",
  data() {
    return {
      setTitle: "",
      setID: "",
      cardIDs: [],
      allSides: [],
      currentSides: [],
    };
  },
  components: {
    CardComponent,
  },
  methods: {
    fetchData() {
      this.setTitle = this.$store.state.setTitle;
      this.setID = this.$store.state.setID;
      this.cardIDs = this.$store.state.cardIDs;
      this.allSides = this.$store.state.allSides;
    },
  },
  created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
      this.$store.commit("setCurrentUser", localStorage.email);
    }
    this.fetchData();

    for (const side of this.allSides) {
      this.currentSides.push(0);
    }
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}
</style>
