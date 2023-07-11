<template>
  <v-dialog width="400px">
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover></v-img>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-icon icon="mdi-close" size="x-large" @click="closeModal"></v-icon>
      </v-card-actions>
      <div v-if="passwordChanged">
        <v-card-title class="justify-center text-h4 mb-5">Password Changed</v-card-title>
        <v-card-text class="text-center">Your password has been changed successfully.</v-card-text>
      </div>
      <div v-else>
        <v-card-title class="justify-center text-h4 mb-5">Change Password</v-card-title>
          <v-text-field
            bg-color="white"
            label="New Password"
            v-model="newPassword"
            type="password"
            :error-messages="passwordErrors"
            @focus = "passwordErrors = []"
            class="mx-5 mb-5"
          ></v-text-field>
          <v-text-field
            bg-color="white"
            label="Confirm New Password"
            type="password"
            v-model="newPasswordConfirmation"
            class="mx-5 mb-16"
          ></v-text-field>
          <v-card-actions class="justify-center mb-4">
            <v-btn class="bg-primaryRed" @click="changePassword">Change Password</v-btn>
          </v-card-actions>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUserStore } from '../stores/user'
import { AxiosError } from 'axios'

const emit = defineEmits(['close'])
const newPassword = ref<string>("")
const newPasswordConfirmation = ref<string>("")
const passwordErrors = ref<string | string[]>('')
const passwordChanged = ref(false)
const userStore = useUserStore()

async function changePassword() {
  if (newPassword.value === newPasswordConfirmation.value) {
    try {
      let status, data = await userStore.changePassword(newPassword.value)
      console.log(status, data)
      if (status === 200) {
        passwordChanged.value = true
      } 
    } catch (error: AxiosError | any) {
      if (error instanceof AxiosError && error.request) {
        passwordErrors.value = JSON.parse(error.request.response).password
      }
    }
  } else {
    passwordErrors.value = "Passwords must match"
  }
}

function closeModal() {
  emit('close')
}
</script>
