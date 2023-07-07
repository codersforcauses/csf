<template>
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="500px">
      <v-card style="height: 100%">
        <form @submit.prevent="submitForm" class="bg-backgroundGrey">
          
          <v-row justify="end">
            <v-col cols="auto">
          <v-btn variant="text" @click="closeModal"><v-icon icon="mdi-close" size="32px"></v-icon></v-btn>
          </v-col>
          </v-row>

          <v-img :src=logo width="100%" cover></v-img>


          <v-col cols="auto">
            <v-row justify="center">
              <v-card-title class="text-center text-h4 pb-2">Welcome Back</v-card-title>
              <v-card-subtitle class="text-center text-subtitle-1">Login to your existing account</v-card-subtitle>
            </v-row>
          </v-col>

          <v-card-text>
            <v-form>
              <v-text-field 
              bg-color="#FFFFFF"
              :rules="[required]"
              v-model="form.email" 
              label="Email"
              required>
            </v-text-field>
              <v-text-field
              bg-color="#FFFFFF"
              :rules="[required]" 
              v-model="form.password" 
              label="Password" 
              type="password"
              required>
            </v-text-field>
            </v-form>
          </v-card-text>
          
          <v-card-actions>
              <v-col cols="auto" justify="center">
                <v-row align="center" justify="center">
                  <v-btn varient="text" 
                  color="secondaryBlue" 
                  style="font-size: 12px">Forgot Password?</v-btn>
                </v-row>       

                <v-row align="center" justify="center">
                  <v-btn variant="text" 
                  class="bg-primaryRed" 
                  @click="submitForm">Login</v-btn>
                </v-row>

                <v-row align="center" justify="center">
                  <v-btn varient="text" 
                  color="secondaryBlue" 
                  style="font-size:12px">Register</v-btn>
                </v-row>
              </v-col>
          </v-card-actions>
        
        </form>
      </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import logo from '../assets/CSF_Logo_RGB.png'

const { mobile } = useDisplay()
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
  closeModal()
}
</script>
