<template>
  <TeamDashboard v-if="user_id && team_id" />
  <CreateOrJoinTeam v-else-if="user_id && !team_id" />
  <LoginModal v-else />
</template>

<script setup lang="ts">
import LoginModal from '../components/LoginModal.vue'
import CreateOrJoinTeam from '../components/teams/CreateOrJoinTeam.vue'
import TeamDashboard from '../components/teams/TeamDashboard.vue'
import { ref, onMounted } from 'vue'

// change these values to show the different modals
const user_id = ref(true)
const team_id = ref(true)

onMounted(async () => {})
</script>
