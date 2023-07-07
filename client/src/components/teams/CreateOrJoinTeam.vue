<template>
  <section :fullscreen="mobile" class="vertical-align" align="center">
    <v-row justify="center" class="ma-8">
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
        <v-text-field id="teamCodeId" class="rounded-t-sm" bg-color="white" label="Team Code" />
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-6 mb-2">
      <v-btn size="large" color="black white--text">Join Team</v-btn>
    </v-row>
    <p>Get the join code from your team leader</p>
  </section>
</template>

<script setup lang="ts">
import { useDisplay } from 'vuetify'
import NewTeamModal from '@/components/teams/NewTeamModal.vue'

const { mobile } = useDisplay()
</script>
