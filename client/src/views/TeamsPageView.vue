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
import { useSubTeamStore } from '@/stores/subTeam'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore();
const subTeamStore = useSubTeamStore()

onMounted(async () => {
  try {
    await subTeamStore.getSubUsers(userStore.user.subteamId);
  } catch (error) {
    console.log(error);
  }
  console.log(subTeamStore.info);
  
})

// change these values to show the different modals
const user_id = ref(true)
const team_id = ref(true)
</script>
