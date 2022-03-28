<template>
  <div class="show-all-sets">
    <p class="text-white font-medium text-5xl mb-8 poppins-font">My sets ...</p>
    <div class="flex flex-col" v-if="card_package.length != 0">
      <CardOverviewComponent
        v-for="(card, index) in card_package"
        v-bind:key="index"
        v-bind:set_title="card['set_name']"
        v-bind:set_id="card['set_id']"
        v-bind:card_ids="card['card_ids']"
        v-bind:sides="card['sides']"
        v-bind:idx="index"
        @deleteSet="setIdToDelete = $event"
      />
    </div>
    <div v-else class="text-white font-medium text-2xl">
      Nothing here yet! Create a
      <router-link to="/create" class="underline font-normal text-yellow-300"
        >new set</router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CardOverviewComponent from "@/components/CardOverviewComponent.vue";

export default {
  name: "ShowAllSetsView",
  data() {
    return {
      email: "",
      setIdToDelete: '',
      cards: {},
      set_cards: {},
      set_names: {},
      card_package: [],
    };
  },
  methods: {},
  components: {
    CardOverviewComponent,
  },
  async created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
      this.$store.commit("setCurrentUser", localStorage.email);

      // Fetch current user's set of cards from the database
      const { data } = await axios.post("http://localhost:5000/fetch_sets", {
        email: this.email,
      });

      const { cards, set_cards, set_names } = JSON.parse(data);
      this.cards = cards;
      this.set_cards = set_cards;
      this.set_names = set_names;

      for (const set_id in set_names) {
        const pkg = {};
        pkg["set_id"] = set_id;
        pkg["set_name"] = set_names[set_id];
        pkg["sides"] = [];
        pkg["card_ids"] = [...set_cards[set_id]];

        for (const card_id of set_cards[set_id]) {
          pkg["sides"].push(cards[card_id]);
        }
        this.card_package.push(pkg);
      }
    }
  },
  watch: {
    setIdToDelete: function(id) {
      console.log(`ID: ${id}`);
      for(const i in this.card_package) {
        if(this.card_package[i].set_id == id) {
          console.log(this.card_package[i]);
          this.card_package.splice(i, 1);
        }
      }
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
