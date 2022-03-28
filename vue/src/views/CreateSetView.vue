<template>
  <div class="create flex flex-col" :class="{ shake: animate }">
    <div class="flex flex-row">
      <h1 class="text-yellow-400 text-5xl font-bold cabin-font m-2 basis-4/5">
        Build a set
      </h1>
      <button
        class="basis-1/5 text-white font-medium rounded-md text-md m-1 text-center dark:bg-green-600 dark:hover:bg-green-700 font-medium poppins-font"
        @click="saveSet"
      >
        SAVE
      </button>
      <button
        class="basis-1/5 text-white font-medium rounded-md text-md m-1 text-center dark:bg-red-600 dark:hover:bg-red-700 font-medium poppins-font"
        @click="goBack"
      >
        CANCEL
      </button>
    </div>
    <label for="setname" class="text-white font-medium text-2xl m-2"
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
    <label for="cardinfo" class="text-white font-medium text-xl m-2"
      >Card information:</label
    >
    <div class="flex flex-row justify-center">
      <button
        class="rounded-full bg-blue-700 p-2 text-blue-100 font-medium text-2xl mb-4 mx-2 basis-1/6  font-medium"
        @click="addComponent"
      >
        +
      </button>
      <button
        class="rounded-full bg-red-600 p-2 text-blue-100 font-medium text-2xl mb-4 mx-2 basis-1/6 font-medium"
        @click="removeComponent"
      >
        -
      </button>
    </div>
    <table id="setCards">
      <tr>
        <th>
          <p class="text-white text-2xl">Side A</p>
        </th>
        <th>
          <p class="text-white text-2xl">Side B</p>
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
      animate: false
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
      if(cardContent != '') {
        console.log(cardContent);
        this.componentDataArray[i][card] = cardContent;
      }
    },
    async saveSet() {
      if(this.setname == "" || this.componentArray.length == 0 || this.componentDataArray.length == 0) {
        this.shakeComponent();
        return;
      }
      try {
        for(let i = 0; i < this.componentDataArray.length; ++i) {
          const { cardA, cardB } = this.componentDataArray[i];
          if(cardA == '' || cardB == '') {
            this.shakeComponent();
            return;
          }
        }
        const payload = {
          setname: this.setname,
          data: this.componentDataArray,
          user_email: localStorage.email
        }
        const { data } = await axios.post("http://localhost:5000/save_set", payload);
        if(data === 'done') {
          this.$router.push('dashboard')
        }
      } catch(e) {
        console.error(e);
      }
    },
    goBack() {
      this.$router.push('dashboard')
    },
    shakeComponent() {
      // Animate vue component: https://codepen.io/aut0maat10/pen/ExaNZNo
      this.animate = true;
      setTimeout(() => {
        this.animate = false;
      }, 1000);
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
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}

.cabin-font {
  font-family: "Cabin", sans-serif;
}

.montserrat-font {
  font-family: "Montserrat", sans-serif;
}

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
