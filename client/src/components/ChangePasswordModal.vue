<template>
  <v-dialog width="400px">
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover></v-img>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-icon icon="mdi-close" size="x-large" @click="closeModal"></v-icon>
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-5">Change Password</v-card-title>
      <v-text-field
        hide-details
        bg-color="white"
        label="New Password"
        v-model="newPassword"
        class="mx-5 mb-5"
      ></v-text-field>
      <v-text-field
        hide-details
        bg-color="white"
        label="Confirm New Password"
        v-model="newPasswordConfirmation"
        class="mx-5 mb-16"
      ></v-text-field>
      <v-card-actions class="justify-center mb-4">
        <v-btn class="bg-primaryRed" @click="changePassword">Change Password</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUserStore } from '../stores/user'
const emit = defineEmits(['close'])
const newPassword = ref("")
const newPasswordConfirmation = ref("")
const userStore = useUserStore()

async function changePassword() {
  try {
    await userStore.changePassword(newPassword.value, newPasswordConfirmation.value);
  } catch (error) {
    console.log(error);
  }
}

function closeModal() {
  emit('close')
}
</script>
