<template>
  <section>
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="500px">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props">New Team</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <v-btn icon @click="closeDialog">
            <span>x</span>
          </v-btn>
              <span class="text-h5 ps-5">New Team</span>
        </v-card-title>
        <form @submit.prevent="submitForm">
          <v-card-text>
            <v-form>
              <v-text-field v-model="form.name" label="Team Name"></v-text-field>
              <v-text-field  v-model="form.bio" label="Bio"></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="submitForm">Create</v-btn>
            <v-btn color="red" @click="closeDialog">Cancel</v-btn>
          </v-card-actions>
        </form>
      </v-card>
    </v-dialog>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

const { mobile } = useDisplay()
const dialog = ref(false)
const form = ref({
  name: '',
  bio: ''
})
const submitForm = () => {
  console.log('Team Name:', form.value.name)
  console.log('Team Bio:', form.value.bio)
  dialog.value = false
}
const closeDialog = () => {
  dialog.value = false
  form.value.name = ''
  form.value.bio = ''
}


</script>