<template>
    <v-btn icon="mdi-plus" @click="dialog = true"/>
    <MileageModal v-model="dialog"></MileageModal>
</template>

<script setup lang="ts">
    import MileageModal from '../components/MileageModal.vue'
    import { ref } from 'vue'
    const dialog = ref(false)
</script>

<style scoped>

</style>