<template>
    <div class="bg-white text-gray-900 w-full m-4 p-6 rounded-md" @click="changeSide">
        <p class="text-gray-900 font-bold text-4xl mb-2" v-if="!switchSide">{{ content[0] }}</p>
        <p class="text-gray-900 font-bold text-4xl mb-2" v-else>{{ content[1] }}</p>
        <p class="text-gray-700 text-sm italic" v-if="!switchSide">Card #{{ idx }}, Side A</p>
        <p class="text-gray-700 text-sm italic" v-else>Card #{{ idx }}, Side B</p>
    </div>
</template>

<script>
export default {
    name: "CardComponent",
    data() {
        return {
            content: [],
            switchSide: false
        }
    },
    props: ['idx', 'sidetext', 'currentside'],
    created() {
        this.content = [this.$props.sidetext["0"], this.$props.sidetext["1"]];
    },
    methods: {
        changeSide() {
            // Also add a global counter (inside vue store) to keep track of read count
            this.switchSide = !this.switchSide;
        }
    }
}
</script>

<style scoped>
</style>
