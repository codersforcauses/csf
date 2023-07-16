<template>
  <v-dialog width="500px">
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="closeModal" />
      </v-card-actions>
      <div v-if="passwordChanged">
        <v-card-title class="justify-center text-h4 mb-5">Password Changed</v-card-title>
        <v-card-text class="text-center">Your password has been changed successfully.</v-card-text>
      </div>
      <div v-else>
        <v-card-title class="justify-center text-h4 mb-5">Change Password</v-card-title>
        <v-text-field
          bg-color="white"
          label="Old Password"
          v-model="state.oldPassword"
          type="password"
          :error-messages="errors.oldPassword"
          @focus="errors.newPassword = ''"
          class="mx-5 mb-5"
        />
        <v-text-field
          bg-color="white"
          label="New Password"
          v-model="state.newPassword"
          type="password"
          :error-messages="errors.newPassword"
          @focus="errors.oldPassword = ''"
          class="mx-5 mb-5"
        />
        <v-text-field
          bg-color="white"
          label="Confirm New Password"
          type="password"
          v-model="state.newPasswordConfirmation"
          class="mx-5 mb-16"
        />
        <v-card-actions class="justify-center mb-4">
          <v-btn class="bg-primaryRed" @click="changePassword">Change Password</v-btn>
        </v-card-actions>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, reactive} from 'vue'
import { useUserStore } from '../stores/user'
import { AxiosError } from 'axios'
import type { ChangePasswordError } from '../types/user'
import camelize from 'camelize-ts';

const emit = defineEmits(['close'])
const state = reactive({
  oldPassword: '',
  newPassword: '',
  newPasswordConfirmation: ''
})
const errors = reactive({
  oldPassword: '',
  newPassword: '',
})

const passwordChanged = ref(false)
const userStore = useUserStore()

async function changePassword() {
  if (state.oldPassword === '') {
    errors.oldPassword = 'You must enter your old password'
  } else if (state.newPassword !== state.newPasswordConfirmation) {
    errors.newPassword = 'Passwords must match'
  }
  else {
    try {
      let status = await userStore.changePassword(state.oldPassword, state.newPassword)
      if (status === 200) {
        passwordChanged.value = true
      }
    } catch (error: AxiosError | any) {
      if (error instanceof AxiosError && error.response && error.response.status === 400) {
        let data = camelize(error.response.data) as ChangePasswordError
        if (data.oldPassword) {
          errors.oldPassword = data.oldPassword
        }
        if (data.password) {
          errors.newPassword = data.password
        }
      }
    }
  }
}

function closeModal() {
  emit('close')
}
</script>
