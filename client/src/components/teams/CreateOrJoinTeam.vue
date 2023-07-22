<template>
  <section :fullscreen="mobile" class="vertical-align pa-1" align="center">
    <v-row justify="center" class="ma-10">
      <h2 style="text-align: center">You are not currently part of a team</h2>
    </v-row>
    <v-row justify="center" class="ma-10">
      <NewTeamModal />
    </v-row>

    <v-container>
      <v-sheet class="ma-0 d-flex justify-center align-center">
        <v-divider thickness="2" length="15vw" />
        <h2 class="ml-8 mr-8">OR</h2>
        <v-divider thickness="2" length="15vw" />
      </v-sheet>
    </v-container>
    <v-row justify="center" class="mt-5">
      <v-col cols="8">
        <v-text-field
          id="teamCodeId"
          class="rounded-t-sm"
          bg-color="white"
          label="Team Code"
          v-model="joinCode"
        />
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-6 mb-5">
      <v-btn size="large" color="black white--text" @click="joinTeam">
        <v-progress-circular
          v-if="loading"
          indeterminate
          size="24"
          color="white"
        ></v-progress-circular>
        <span v-else>JOIN TEAM</span>
      </v-btn>
    </v-row>
    <v-row justify="center" class="mt-5 mb-5">
      <p>Get the join code from your team leader</p>
    </v-row>
  </section>
</template>

<script setup lang="ts">
import { useDisplay } from 'vuetify'
import NewTeamModal from '@/components/teams/NewTeamModal.vue'
import { ref } from 'vue'
import { useTeamStore } from '@/stores/team'

const loading = ref(false)
const teamStore = useTeamStore()
const joinCode = ref('')

const joinTeam = async () => {
  loading.value = true
  try {
    await teamStore.joinTeam(joinCode.value)
  } catch (error) {
    console.error("Error joining team:", error)
  } finally {
    loading.value = false
  }
}


const { mobile } = useDisplay()
</script>
