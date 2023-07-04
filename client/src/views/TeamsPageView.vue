<template>
  <div>
    <template v-if="user_id && team_id">
      <TeamDashboard />
    </template>
    <template v-else-if="user_id && !team_id">
      <CreateOrJoinTeam />
    </template>
    <template v-else>
      <LoginModal />
    </template>
  </div>
</template>

<script setup lang="ts">
import LoginModal from '../components/LoginModal.vue'
import CreateOrJoinTeam from '../components/teams/CreateOrJoinTeam.vue'
import TeamDashboard from '../components/teams/TeamDashboard.vue'
import { ref } from 'vue'

// change these values to show the different modals
const user_id = ref(true)
const team_id = ref(true)
</script>
