<template>
  <section>
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="960px">
      <template v-slot:activator="{ props }">
        <v-btn size="large" color="red white--text" v-bind="props">New Team</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <v-row>
            <v-col>
              <span id="new-team" class="text-h5 ps-5">New Team</span>
            </v-col>
            <v-col align="end">
              <v-icon class="mdi mdi-close" @click="closeDialog"></v-icon>
            </v-col>
          </v-row>
        </v-card-title>
        <form @submit.prevent="submitForm">
          <v-card-text>
            <v-form>
              <v-text-field v-model="form.name" label="Team Name"></v-text-field>
              <v-textarea v-model="form.bio" label="Bio"></v-textarea>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-row>
              <v-btn size="large" justify="center" bg-color="red" @click="submitForm">Create</v-btn>
            </v-row>
          </v-card-actions>
        </form>
      </v-card>
    </v-dialog>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import { useTeamStore } from '@/stores/team'

const teamStore = useTeamStore()

const { mobile } = useDisplay()
const dialog = ref(false)
const form = ref({
  name: '',
  bio: ''
})

// formValidation = check if team name already exists

const submitForm = () => {
  console.log('Team Name:', form.value.name)
  console.log('Team Bio:', form.value.bio)
  console.log('Team_id:', 'unique id_1')
  console.log('Join Code:', 'unique id_2')

  teamStore.createTeam({ ...form.value })
}

const closeDialog = () => {
  dialog.value = false
  form.value.name = ''
  form.value.bio = ''
}
</script>
