<template>
  <v-icon
    v-if="user.teamAdmin"
    icon="mdi mdi-pencil"
    size="32px"
    color="black"
    @click="editTeamInfoDialog = true"
  />
  <v-dialog
    v-model="editTeamInfoDialog"
    :fullscreen="isFullscreen"
    max-width="500px"
    max-height="100vh"
  >
    <v-card class="bg-backgroundGrey">
      <v-img
        src="/images/Footer-min.jpeg"
        width="100%"
        max-height="16"
        alt="red background"
        cover
      />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="closeDialog" />
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-6">Edit Team</v-card-title>
      <form class="pb-0 mb-0 mx-8">
        <v-text-field bg-color="white" label="Event Name" v-model="newTeamName" class="mx-5" />
        <v-textarea bg-color="white" label="Description" v-model="newBioText" class="mx-5" />
        <v-card-actions class="justify-center mb-4">
          <v-btn variant="elevated" color="primaryRed" @click="editTeamInfo">Save Changes</v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import { useTeamStore } from '@/stores/team'
import { storeToRefs } from 'pinia'
const teamStore = useTeamStore()
const { user, team } = storeToRefs(teamStore)

const isFullscreen = ref(false)

const editTeamInfoDialog = ref(false)
const newBioText = ref(team.value ? team.value.bio : '')
const newTeamName = ref(team.value ? team.value.name : '')

const editTeamInfo = async () => {
  teamStore.editTeam({ name: newTeamName.value, bio: newBioText.value })
  editTeamInfoDialog.value = false
}

const closeDialog = () => {
  editTeamInfoDialog.value = false
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
