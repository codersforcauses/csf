<template>
  <section>
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="500px">
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
            <v-btn color="primary" @click="closeModal">Cancel</v-btn>
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
const dialog = ref(true)

const form = ref({
  email: '',
  password: ''
})

defineProps(['loginModal'])
const emit = defineEmits(['openLoginModal'])

const closeModal = () => {
  emit('openLoginModal', false)
}

const submitForm = () => {
  console.log('Email:', form.value.email)
  console.log('Password:', form.value.password)

  userStore.loginUser(form.value.email, form.value.password)

  closeModal()
}
</script>
