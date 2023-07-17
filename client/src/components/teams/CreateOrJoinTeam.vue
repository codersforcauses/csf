<template>
  <section :fullscreen="mobile" class="vertical-align pa-10" align="center">
    <v-row justify="center" class="mb-10">
      <h2>You are not currently part of a team</h2>
    </v-row>
    <NewTeamModal />
    <v-container>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-row align="center" class="ma-0" no-gutters>
          <v-col>
            <v-divider thickness="2" />
          </v-col>

          <v-col cols="2">
            <h2>OR</h2>
          </v-col>

          <v-col>
            <v-divider thickness="2" />
          </v-col>
        </v-row>
      </v-col>
    </v-container>
    <v-row justify="center">
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
      <v-btn size="large" color="black white--text" @click="joinTeam">Join Team</v-btn>
    </v-row>
    <p>Get the join code from your team leader</p>
  </section>
</template>

<script setup lang="ts">
import { useDisplay } from 'vuetify'
import NewTeamModal from '@/components/teams/NewTeamModal.vue'
import { ref } from 'vue'
import { useTeamStore } from '@/stores/team'
import { storeToRefs } from 'pinia'
const teamStore = useTeamStore()

const { user } = storeToRefs(teamStore)

const joinCode = ref('')

const joinTeam = () => {
  teamStore.joinTeam(user.value.id, joinCode.value)
}

const { mobile } = useDisplay()
</script>
