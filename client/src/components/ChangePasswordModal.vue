<template>
  <v-dialog width="500px">
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
        <v-icon icon="mdi-close" size="x-large" @click="closeModal" />
      </v-card-actions>
      <div v-if="passwordChanged">
        <v-card-title class="justify-center text-h4 mb-5">Password Changed</v-card-title>
        <v-card-text class="text-center">Your password has been changed successfully.</v-card-text>
      </div>
      <div v-else>
        <v-card-title class="justify-center text-h4 mb-5">Change Password</v-card-title>
        <v-container>
          <v-row dense>
            <v-col cols="12">
              <v-text-field
                bg-color="white"
                label="Old Password"
                v-model="state.oldPassword"
                type="password"
                :error-messages="errors.oldPassword"
                @focus="errors.newPassword = ''"
              />
            </v-col>
            <v-col cols="12">
              <v-text-field
                bg-color="white"
                label="New Password"
                v-model="state.newPassword"
                type="password"
                :error-messages="errors.newPassword"
                @focus="errors.oldPassword = ''"
              />
            </v-col>
            <v-col cols="12">
              <v-text-field
                bg-color="white"
                label="Confirm New Password"
                type="password"
                v-model="state.newPasswordConfirmation"
              />
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions class="justify-center mb-4">
          <v-btn class="bg-primaryRed" @click="changePassword">
                <v-progress-circular
                  v-if="loading"
                  indeterminate
                  size="24"
                  color="white"
                ></v-progress-circular>
                <span v-else>Change Password</span>
          </v-btn>
        </v-card-actions>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useUserStore } from '../stores/user'
import { AxiosError } from 'axios'
import type { ChangePasswordError } from '../types/user'
import camelize from 'camelize-ts'
import { notify } from '@kyvg/vue3-notification'

const emit = defineEmits(['close'])
const state = reactive({
  oldPassword: '',
  newPassword: '',
  newPasswordConfirmation: ''
})
const errors = reactive({
  oldPassword: '',
  newPassword: ''
})

const passwordChanged = ref(false)
const userStore = useUserStore()
const loading = ref(false)

async function changePassword() {
  loading.value = true
  if (state.oldPassword === '') {
    errors.oldPassword = 'You must enter your old password'
  } else if (state.newPassword !== state.newPasswordConfirmation) {
    errors.newPassword = 'Passwords must match'
  } else {
    try {
      let status = await userStore.changePassword(state.oldPassword, state.newPassword)
      if (status === 200) {
        passwordChanged.value = true
        notify({
          title: 'Password Change',
          type: 'success',
          text: 'Password Changed Successful'
        })
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
        notify({
          title: 'Password Change',
          type: 'error',
          text: 'Password Change Error'
        })
      }
    }
  }
  loading.value = false
}

function closeModal() {
  emit('close')
}
</script>
