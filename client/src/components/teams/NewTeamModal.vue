<template>
  <v-dialog v-model="dialog" :fullscreen="isFullscreen" max-width="500px" max-height="100vh">
    <template v-slot:activator="{ props: dialog }">
      <v-btn size="large" color="red white--text" v-bind="dialog">New Team</v-btn>
    </template>
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" alt="red background" cover />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="closeDialog" />
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-6">Create Team</v-card-title>
      <form class="pb-0 mb-0 mx-8">
        <v-text-field bg-color="white" label="Team Name" v-model="form.name" class="mx-5" />
        <v-textarea bg-color="white" label="Bio" v-model="form.bio" class="mx-5" />
        <v-card-actions class="justify-center mb-4">
          <v-btn variant="elevated" color="primaryRed" @click="submitForm">Create</v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import { useTeamStore } from '@/stores/team'

const teamStore = useTeamStore()

const isFullscreen = ref(false)

const dialog = ref(false)
const form = ref({
  name: '',
  bio: ''
})

// formValidation = check if team name already exists

const submitForm = () => {
  teamStore.createTeam({ ...form.value })
}

const openDialog = () => {
  dialog.value = true
}

const closeDialog = () => {
  dialog.value = false
  form.value.name = ''
  form.value.bio = ''
}

watchEffect(async () => {
  const updateFullscreen = async () => {
    isFullscreen.value = window.innerWidth <= 500
  }

  await updateFullscreen()

  window.addEventListener('resize', updateFullscreen)
  return () => {
    window.removeEventListener('resize', updateFullscreen)
  }
})
</script>
