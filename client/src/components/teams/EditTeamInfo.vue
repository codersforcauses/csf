<template>
  <v-icon
    v-if="user.teamAdmin"
    icon="mdi mdi-pencil"
    size="32px"
    color="black"
    @click="editTeamInfoDialog = true"
  />
  <v-dialog v-model="editTeamInfoDialog" width="auto">
    <v-card>
      <v-card-text>What would you like to set the team name and bio to?</v-card-text>
      <v-text-field v-model="newTeamName" placeholder="Team Name"></v-text-field>
      <v-textarea v-model="newBioText" placeholder="Bio"></v-textarea>
      <v-card-actions>
        <v-btn @click="editTeamInfo">Submit</v-btn>
        <v-btn @click="editTeamInfoDialog = false">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useTeamStore } from '@/stores/team'
import { storeToRefs } from 'pinia'
const teamStore = useTeamStore()
const { user, team } = storeToRefs(teamStore)

const editTeamInfoDialog = ref(false)
const newBioText = ref(team.value ? team.value.bio : '')
const newTeamName = ref(team.value ? team.value.name : '')

const editTeamInfo = async () => {
  teamStore.editTeam({ name: newTeamName.value, bio: newBioText.value })
  editTeamInfoDialog.value = false
}
</script>
