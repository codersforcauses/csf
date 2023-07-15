<template>
    <div class="header">
        <h1 class="text-center text-secondaryTint font-weight-medium text-md-h1" id="title">Leaderboards</h1>
    </div>
    <v-row class="ma-0 pt-4" justify="space-evenly">
        <v-btn
            variant="flat"
            density="compact"
            width="120px"
            :color="activeButton === board ? 'rgb(52, 94, 158, 0.3)' : ''"
            :class="activeButton === board ? 'text-secondaryBlue' : 'black'"
            v-for="board in ['Individual', 'Teams']"
            :key="board"
            rounded="xl"
            @click="activeButton = board">{{ board }}</v-btn>
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
  font-family: Hackney!important;
}

#title {
    font-family: Hackney!important;
}
</style>
