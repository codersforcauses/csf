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

import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

const userStore = useUserStore()

const { user } = storeToRefs(userStore)

onMounted(async () => {})
</script>
