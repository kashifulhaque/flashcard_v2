<template>
  <div class="create flex flex-col">
    <div class="flex flex-row">
      <h1 class="text-white text-4xl font-bold cabin-font m-2 basis-4/5">
        Create a new Set
      </h1>
      <button
        class="basis-1/5 text-white font-medium rounded-md text-md m-1 text-center dark:bg-green-600 dark:hover:bg-green-700"
        @click="saveSet"
      >
        SAVE
      </button>
    </div>
    <label for="setname" class="text-white font-medium text-xl m-2"
      >Set name:</label
    >
    <input
      type="text"
      name="setname"
      id="setname"
      v-model="setname"
      class="mx-2 mb-2 h-12 p-2 montserrat-font"
      placeholder="Set name goes here ..."
    />
    <label for="cardinfo" class="text-white font-medium text-md m-2"
      >Card information:</label
    >
    <div class="flex flex-row justify-center">
      <button
        class="rounded-full bg-blue-700 p-3 text-blue-100 font-medium text-xl mb-4 mx-2 basis-1/4"
        @click="addComponent"
      >
        + new card
      </button>
      <button
        class="rounded-full bg-red-600 p-3 text-blue-100 font-medium text-xl mb-4 mx-2 basis-1/4"
        @click="removeComponent"
      >
        - remove card
      </button>
    </div>
    <table id="setCards">
      <tr>
        <th>
          <p class="text-white text-xl">Side A</p>
        </th>
        <th>
          <p class="text-white text-xl">Side B</p>
        </th>
      </tr>
      <CardContentComponent
        v-for="(comp, index) in componentArray"
        v-bind:key="index"
        v-bind:content="componentDataArray[index]"
        v-on:get-card-data="gotCardData($event, index)"
      />
    </table>
  </div>
</template>

<script>
import CardContentComponent from "@/components/CardContentComponent.vue";
import axios from 'axios';

export default {
  name: "CreateSetView",
  data() {
    return {
      setname: "",
      componentArray: [],
      componentDataArray: [],
    };
  },
  methods: {
    addComponent() {
      const component = {
        component: CardContentComponent,
      };
      const componentData = {
        cardA: "",
        cardB: "",
      };

      this.componentArray.push(component);
      this.componentDataArray.push(componentData);
    },
    removeComponent() {
      this.componentArray.pop();
      this.componentDataArray.pop();
    },
    gotCardData(e, i) {
      const { card, cardContent } = e;
      this.componentDataArray[i][card] = cardContent;
    },
    async saveSet() {
      console.log(this.componentDataArray);
      try {
        const payload = {
          setname: this.setname,
          data: this.componentDataArray,
          user_email: localStorage.email
        }
        const { data } = await axios.post("http://localhost:5000/save_set", payload);
        console.log(data);
      } catch(e) {
        console.error(e);
      }
    }
  },
  components: {
    CardContentComponent,
  },
  created() {
    if (!localStorage.email) {
      this.$router.push("/");
    } else {
      this.email = localStorage.email;
    }
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@600&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap");

.cabin-font {
  font-family: "Cabin", sans-serif;
}

.montserrat-font {
  font-family: "Montserrat", sans-serif;
}
</style>
