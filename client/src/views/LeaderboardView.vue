<template>
    <div class="header">
        <h1 class="text-center text-secondaryTint">Leaderboards</h1>
    </div>
    <v-row class="ma-0">
        <v-chip
            :color="activeButton === board ? 'secondaryBlue' : ''"
            v-for="board in ['Individual', 'Teams']"
            :key="board"
            rounded="xl"
            @click="activeButton = board">{{ board }}</v-chip>
    </v-row>
</template>

<script setup lang="ts">
    import { ref } from 'vue'

    const activeButton = ref('Individual')
</script>

<style>
    .header {
        background-image: url('/images/Footer-min.jpeg');
        background-size: cover;
    }
</style>