<template>
  <TeamDashboard v-if="user && user.teamId" />
  <CreateOrJoinTeam v-else-if="user && !user.teamId" />
  <LoginModal v-else />
</template>

<script setup lang="ts">
import LoginModal from '../components/LoginModal.vue'
import CreateOrJoinTeam from '../components/teams/CreateOrJoinTeam.vue'
import TeamDashboard from '../components/teams/TeamDashboard.vue'
import { onMounted } from 'vue'
import { useSubTeamStore } from '@/stores/subTeam'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'
const userStore = useUserStore()
const subTeamStore = useSubTeamStore()

const { user } = storeToRefs(userStore)

onMounted(async () => {
  // try {
  //   await subTeamStore.getSubUsers(user.value?.teamId)
  //   console.log(`here is the userid`);
  //   console.log(user.value?.teamId)
  // } catch (error) {
  //   console.log(error)
  // }
})

onMounted(async () => {})
</script>
