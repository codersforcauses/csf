<template>
    <section>
      <v-dialog v-model="dialog" :fullscreen="mobile" max-width="500px">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props">Login</v-btn>
        </template>
        <v-card>
          <form @submit.prevent="submitForm">
            <v-card-title>
              <span class="text-h5">Login</span>
            </v-card-title>
            <v-card-text>
              <v-form>
                <v-text-field v-model="email" label="Email"></v-text-field>
                <v-text-field v-model="password" label="Password" type="password"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="submitForm">Submit</v-btn>
              <v-btn color="primary" @click="closeDialog">Cancel</v-btn>
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
  const email = ref('')
  const password = ref('')
  
  const submitForm = () => {
    console.log('Email:', email.value)
    console.log('Password:', password.value)
    dialog.value = false
  }
  
  const closeDialog = () => {
    dialog.value = false
  }
  
  const setup = () => {
    return {
      dialog,
      email,
      password,
      submitForm,
      closeDialog
    }
  }
  </script>
  