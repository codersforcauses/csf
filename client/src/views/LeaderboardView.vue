<template>
  <div class="header">
    <h1 class="text-center text-secondaryTint">Leaderboards</h1>
  </div>
  <v-row class="ma-0 justify-center">
    <v-chip
      :color="activeButton === board ? 'secondaryBlue' : ''"
      v-for="board in ['Individual', 'Teams']"
      :key="board"
      rounded="xl"
      @click="activeButton = board"
      >{{ board }}</v-chip
    >
  </v-row>
  <v-row class="ma-0 pa-4">
    <v-text-field
      prepend-inner-icon="mdi-magnify"
      hide-details
      variant="outlined"
      placeholder="Search Leaderboard"
      class="mx-3"
      clearable
      v-model="searchQuery"
    />
  </v-row>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const activeButton = ref('Individual')
const searchQuery = ref('')
</script>

<style>
.header {
  background-image: url('/images/Footer-min.jpeg');
  background-size: cover;
}
</style>
