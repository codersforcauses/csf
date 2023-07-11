<template>
  <v-dialog v-model="dialog" :fullscreen="mobile" max-width="500px">
    <v-card style="height: 100%" class="bg-backgroundGrey">
      <div class="bg-backgroundGrey">
        <v-container class="pa-0">
          <v-img src="/images/Footer-min.jpeg" width="100%" height="10" cover></v-img>
        </v-container>

        <v-row justify="end">
          <v-col v-if="page > 1 && page < 4" cols="auto">
            <v-btn variant="plain" @click="page--"
              ><v-icon icon="mdi-arrow-left" size="32px"></v-icon
            ></v-btn>
          </v-col>
          <v-spacer />
          <v-col cols="auto">
            <v-btn variant="plain" @click="closeModal"
              ><v-icon icon="mdi-close" size="32px"></v-icon
            ></v-btn>
          </v-col>
        </v-row>

        <v-img src="/images/CSF_Logo_RGB.png" width="100%" height="120" contain></v-img>
      </div>
      <div v-if="page === 1">
        <form @submit.prevent="submitForm" class="bg-backgroundGrey">
          <v-col cols="auto">
            <v-row justify="center">
              <v-card-title class="text-center text-h4 pb-2 pt-5">Welcome Back</v-card-title>
              <v-card-subtitle class="text-center text-subtitle-1 pb-5"
                >Login to your existing account</v-card-subtitle
              >
            </v-row>
          </v-col>

          <v-card-text class="pb-0 mb-0">
            <v-form>
              <v-text-field
                bg-color="#FFFFFF"
                :rules="[required]"
                v-model="form.username"
                label="Username"
                required
              />
              <v-text-field
                bg-color="#FFFFFF"
                :rules="[required]"
                v-model="form.password"
                label="Password"
                type="password"
                required
              />
            </v-form>
          </v-card-text>

          <v-row align="center" justify="center">
            <v-btn class="pb-15 mt-0" variant="plain" color="secondaryBlue" style="font-size: 12px" @click="page = 2"
              >Forgot Password?</v-btn
            >
          </v-row>

          <v-card-actions class="justify-center">
            <v-col cols="auto">
              <v-row align="center" justify="center" class="p-10">
                <v-btn variant="flat" class="bg-primaryRed" @click="submitForm">Login</v-btn>
              </v-row>

              <v-row align="center" justify="center">
                <p>
                  or<v-btn variant="plain" color="secondaryBlue" style="font-size: 12px"
                    >Register</v-btn
                  >
                </p>
              </v-row>
            </v-col>
          </v-card-actions>
        </form>
      </div>
      <div v-else-if="page === 2" class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center"> 
            <v-card-title class="text-center text-h4 pb-2 pt-5">Forgot Password?</v-card-title>
            <v-card-subtitle class="text-center text-subtitle-2 pb-5">
              We'll send you reset instructions
            </v-card-subtitle>
          </v-row>  
        </v-col>
        <v-card-text>
          <v-text-field class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required, emailRule]"
            v-model="form.email"
            label="Email"
            clearable
            required
          />
        </v-card-text>
        <v-card-actions class="justify-center mb-5">
          <v-btn variant="flat" class="bg-primaryRed" @click="emailUser">Send Email</v-btn>
        </v-card-actions>
      </div>
      <div v-else-if="page === 3" class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center"> 
            <v-card-title class="text-center text-h4 pb-2 pt-5">Confirm Your Identity</v-card-title>
            <v-card-subtitle class="text-center text-subtitle-1 pb-5">
              Enter the token emailed to you
            </v-card-subtitle>
          </v-row>  
        </v-col>
        <v-card-text>
          <v-text-field class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required]"
            :error-messages="errors.token"
            v-model="form.token"
            label="Token"
            clearable
            required
          />
        </v-card-text>
        <v-card-actions class="justify-center mb-5" align="center">
          <v-btn variant="text" class="mx-2" @click="emailUser">Resend Email</v-btn>
          <v-btn variant="flat" class="mx-2" rounded="lg" color="primaryRed" @click="submitToken">Submit</v-btn>
        </v-card-actions>
      </div>
      <div v-else-if="page === 4" class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center"> 
            <v-card-title class="text-center text-h4 pb-2 pt-5">Create New Password</v-card-title>
          </v-row>  
        </v-col>
        <v-card-text>
          <v-text-field class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required]"
            :error-messages="errors.newPassword"
            v-model="form.newPassword"
            label="Password"
            type="password"
            clearable
            required
          />
          <v-text-field class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required]"
            :error-messages="errors.confirmPassword"
            v-model="form.confirmPassword"
            label="Confirm Password"
            type="password"
            clearable
            required
          />
        </v-card-text>
        <v-card-actions class="justify-center mb-5">
          <v-btn variant="flat" class="mx-2" rounded="lg" color="primaryRed" @click="submitNewPassword">Done</v-btn>
        </v-card-actions>
      </div>
      <div v-else class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center"> 
            <v-card-title class="text-center text-h4 pb-2 pt-5">Success!</v-card-title>
            <v-card-subtitle class="text-center text-subtitle-2 pb-5">
              Your password was changed successfully
            </v-card-subtitle>
          </v-row>  
        </v-col>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import { useUserStore } from '../stores/user'

const { mobile } = useDisplay()
const dialog = ref(true)
const userStore = useUserStore()
const page = ref<1 | 2 | 3 | 4 | 5>(1)

const form = ref({
  username: '',
  password: '',
  email: '',
  token: '',
  newPassword: '',
  confirmPassword: ''
})

const errors = ref({
  token: '',
  newPassword: '',
  confirmPassword: '',
})

defineProps(['loginModal'])
const emit = defineEmits(['openLoginModal'])

const required = (v: string) => !!v || 'Field is required'
const emailRule = (v: string) => isEmail(v) || 'E-mail must be valid'

function isEmail(candidate: string) {
  return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(candidate)
}

const closeModal = () => {
  emit('openLoginModal', false)
}

const submitForm = async () => {
  console.log('Username:', form.value.username)
  console.log('Password:', form.value.password)
  await userStore.loginUser(form.value.username, form.value.password)
  closeModal()
}

async function emailUser() {
  if (isEmail(form.value.email)) {
    await userStore.sendResetEmail(form.value.email)
    page.value = 3;
  }
}

async function submitToken() {
  let res = await userStore.submitResetToken(form.value.token)
  if (res === "Success") {
    errors.value.token = ''
    page.value = 4
  } else {
    errors.value.token = "Invalid token"
  }
}
async function submitNewPassword() {
  if (form.value.newPassword === form.value.confirmPassword) {
    errors.value.newPassword = ''
    errors.value.confirmPassword = ''
    let res = await userStore.submitNewPassword(form.value.token, form.value.newPassword)
    if (res === "Success") {
      page.value = 5
    } else {
      errors.value.newPassword = res
    }
  } else {
    errors.value.newPassword = "Passwords do not match"
    errors.value.confirmPassword = 'Passwords do not match'
  }
}
</script>
