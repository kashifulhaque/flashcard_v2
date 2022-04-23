<template>
  <div
    class="card-overview p-6 mt-2 mb-2 w-full bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-600 dark:border-gray-700"
  >
    <p class="mb-2 text-7xl font-normal tracking-tight dark:text-gray-500">
      #{{ idx + 1 }}
      <span class="text-4xl text-white font-bold">{{ set_title }}</span>
    </p>
    <hr class="text-cyan-400" />
    <p class="mt-2 font-serif text-lg italic font-medium dark:text-gray-200">
      {{ cardIDs.length }} cards with {{ cardIDs.length * 2 }} sides
    </p>

    <button
      class="w-1/5 mt-4 text-white font-medium rounded-md text-md p-2 text-center dark:bg-green-600 dark:hover:bg-green-700 font-medium poppins-font"
      @click="readSet"
    >
      READ 📖
    </button>

    <button
      class="w-1/5 mt-4 ml-2 text-white font-medium rounded-md text-md p-2 text-center dark:bg-black dark:hover:bg-gray-700 font-medium poppins-font"
      @click="exportJSON"
    >
      EXPORT (JSON) 📎
    </button>

    <button
      class="w-1/5 mt-4 ml-2 text-white font-medium rounded-md text-md p-2 text-center dark:bg-black dark:hover:bg-gray-700 font-medium poppins-font"
      @click="exportCSV"
    >
      EXPORT (CSV) 📎
    </button>

    <button
      class="w-1/5 mt-4 ml-2 text-white font-medium rounded-md text-md p-2 text-center dark:bg-red-800 dark:hover:bg-red-500 font-medium poppins-font"
      @click="deleteSet(set_id)"
    >
      DELETE 🗑
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CardOverviewComponent",
  data() {
    return {
      setTitle: "",
      setID: "",
      cardIDs: [],
      allSides: [],
    };
  },
  methods: {
    readSet() {
      this.$store.commit("changeSetTitle", this.setTitle);
      this.$store.commit("changeSetID", this.setID);
      this.$store.commit("changeCardID", this.cardIDs);
      this.$store.commit("changeAllSides", this.allSides);
      this.$router.push("read-card");
    },
    exportJSON() {
      const data = JSON.stringify(this.allSides);
      const blob = new Blob([data], { type: "text/plain" });

      const e = document.createEvent("MouseEvents");
      const a = document.createElement("a");
      a.download = "export.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");

      e.initEvent(
        "click",
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
      );
      a.dispatchEvent(e);
    },
    exportCSV() {
      var array = typeof this.allSides != "object" ? JSON.parse(this.allSides) : this.allSides;
      var str = "";

      for (var i = 0; i < array.length; i++) {
        var line = "";
        for (var index in array[i]) {
          if (line != "") line += ",";

          line += array[i][index];
        }

        str += line + "\r\n";
      }

      var downloadLink = document.createElement("a");
      var blob = new Blob(["\ufeff", str]);
      var url = URL.createObjectURL(blob);
      downloadLink.href = url;
      downloadLink.download = 'export.csv';

      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    },
    async deleteSet(setID) {
      const { data } = await axios.post("http://localhost:5000/delete_set", {
        email: localStorage.email,
        set_id: setID,
      });
      if (data == "Delete") {
        this.$emit("deleteSet", setID);
      }
    },
  },
  props: ["set_title", "set_id", "card_ids", "sides", "idx"],
  created() {
    this.setTitle = this.$props.set_title;
    this.setID = this.$props.set_id;
    this.cardIDs = this.$props.card_ids;
    this.allSides = this.$props.sides;
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap");

.poppins-font {
  font-family: "Poppins", sans-serif;
}
</style>
