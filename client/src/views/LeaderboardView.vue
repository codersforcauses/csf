<template>
    <div class="header">
        <h1 class="text-center text-secondaryTint">Leaderboards</h1>
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

  <v-table fixed-header>
    <thead>
      <tr>
        <th class="text-left">Name</th>
        <th class="text-left">Calories</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in teams" :key="item.name">
        <td>{{ item.name }}</td>
        <td>{{ item.rank }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const activeButton = ref('Individual')
const searchQuery = ref('')
const teams = [
  { name: 'Team 1', rank: 1, mileage: 100 },
  { name: 'Team 2', rank: 2, mileage: 90 },
  { name: 'Team 3', rank: 3, mileage: 80 },
  { name: 'Team 4', rank: 4, mileage: 70 },
  { name: 'Team 5', rank: 5, mileage: 60 },
  { name: 'Team 6', rank: 6, mileage: 50 },
  { name: 'Team 7', rank: 7, mileage: 40 },
  { name: 'Team 8', rank: 8, mileage: 30 },
  { name: 'Team 9', rank: 9, mileage: 20 },
  { name: 'Team 10', rank: 10, mileage: 10 },
  { name: 'Team 11', rank: 11, mileage: 0 },
  { name: 'Team 12', rank: 12, mileage: 0 },
  { name: 'Team 13', rank: 13, mileage: 0 },
  { name: 'Team 14', rank: 14, mileage: 0 },
  { name: 'Team 15', rank: 15, mileage: 0 },
  { name: 'Team 16', rank: 16, mileage: 0 },
  { name: 'Team 17', rank: 17, mileage: 0 },
  { name: 'Team 18', rank: 18, mileage: 0 },
  { name: 'Team 19', rank: 19, mileage: 0 },
  { name: 'Team 20', rank: 20, mileage: 0 }
]
</script>

<style>
.header {
  background-image: url('/images/Footer-min.jpeg');
  background-size: cover;
}
</style>
