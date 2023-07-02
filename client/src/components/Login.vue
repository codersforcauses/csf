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
              <v-text-field v-model="form.email" label="Email"></v-text-field>
              <v-text-field v-model="form.password" label="Password" type="password"></v-text-field>
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
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

const { mobile } = useDisplay()
const userStore = useUserStore()
const { user } = storeToRefs(userStore)

// onMounted(async () => {
//   await userStore.getUser()
// })

const dialog = ref(false)

const form = ref({
  email: '',
  password: ''
})

const submitForm = async () => {
  console.log('Email:', form.value.email)
  console.log('Password:', form.value.password)
  await userStore.loginUser(form.value.email, form.value.password)
  closeDialog()
}

const closeDialog = () => {
  dialog.value = false
}
</script>
