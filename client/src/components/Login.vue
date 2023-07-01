<template>
  <v-model fullscreen :scrim="false">
    <v-col>
      <v-row justify="center">
        <v-container>
          <v-row justify="end">
            <RouterLink to="/"><v-icon>mdi-close</v-icon></RouterLink>
          </v-row>
        </v-container>
      </v-row>

      <v-row justify="center">
        <v-img :src="image" :max-width="250" />
      </v-row>

      <v-row justify="center">
        <v-form @submit.prevent="submitForm">
          <v-container>
            <v-row justify="center">
              <span class="text-h3 text-center">Welcome Back</span>
            </v-row>
            <v-row justify="center">
              <span class="text-h6">Login to your existing account</span>
            </v-row>
          </v-container>
          <v-container>
            <v-form>
              <v-text-field v-model="form.email" label="Email"></v-text-field>
              <v-text-field v-model="form.password" label="Password" type="password"></v-text-field>
              <v-row justify="center">
                <RouterLink to="/">Forgot Password?</RouterLink>
              </v-row>
            </v-form>
          </v-container>
          <v-container class="mt-10">
            <v-col>
              <v-row justify="center">
                <v-btn color="red" @click="submitForm">Login</v-btn>
              </v-row>
              <v-row justify="center">
                <p>or <RouterLink to="/">Register</RouterLink></p>
              </v-row>
            </v-col>
          </v-container>
        </v-form>
      </v-row>
    </v-col>
  </v-model>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import image from '../assets/CSF_Logo_RGB.png'

const dialog = ref(false)

const form = ref({
  email: '',
  password: ''
})

const submitForm = () => {
  console.log('Email:', form.value.email)
  console.log('Password:', form.value.password)
  closeDialog()
}

const closeDialog = () => {
  dialog.value = false
}
</script>
