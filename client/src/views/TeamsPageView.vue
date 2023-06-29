<template>
  <section class="flex-row">
    <v-btn to="/">Home</v-btn>
    <h1>This is the teams landing page</h1>
    <br />
  </section>
  <section :fullscreen="mobile" align="center">
    <!-- add ternary for whether or not to display this -->
    <h2>You are not currently part of a team</h2>
    <br />
    <NewTeamModal />
    <br />
    <h2>-----------OR-----------</h2>
    <br />
    <input type="text" placeholder="Enter Team Code" style="border: 2px solid black; border-radius: 5%;"/>
    <br />
    <br />
    <v-btn>Join Team</v-btn>
  </section>
</template>

<script setup lang="ts">
import { useDisplay } from 'vuetify'

import NewTeamModal from '../components/teams/NewTeamModal.vue'

const { mobile } = useDisplay()
</script>
