<template>
  <v-dialog
    v-model="modalStore.isLogin"
    :fullscreen="isFullscreen"
    max-width="500px"
    max-height="100vh"
  >
    <v-card class="bg-backgroundGrey" align="center" justify="center">
      <div class="bg-backgroundGrey">
        <v-container class="pa-0">
          <v-img
            src="/images/Footer-min.jpeg"
            width="100%"
            height="10"
            alt="red background"
            cover
          />
        </v-container>

        <v-row justify="end">
          <v-col v-if="page > 1 && page < 4" cols="auto">
            <v-btn variant="plain" @click="page--">
              <v-icon icon="mdi-arrow-left" size="32px" />
            </v-btn>
          </v-col>
          <v-spacer />
          <v-col cols="auto">
            <v-btn variant="plain" @click="modalStore.close">
              <v-icon icon="mdi-close" size="32px" />
            </v-btn>
          </v-col>
        </v-row>

        <v-img src="/images/CSF_Logo_RGB.png" width="100%" height="120" contain />
      </div>
      <div v-if="page === 1">
        <v-col cols="auto" class="my-4">
          <v-row justify="center">
            <v-card-title class="text-center text-h4">Welcome Back</v-card-title>
            <v-card-subtitle class="text-center text-subtitle-1 pb-5">
              Login to your existing account
            </v-card-subtitle>
          </v-row>
        </v-col>

        <v-card-text class="pb-0 mb-0 mx-8">
          <v-text-field
            bg-color="#FFFFFF"
            :rules="[required]"
            :error-messages="errors.login"
            @focus="errors.login = ''"
            v-model="modalStore.username"
            label="Username"
            required
          />
          <v-text-field
            bg-color="#FFFFFF"
            :rules="[required]"
            @focus="errors.login = ''"
            v-model="modalStore.password"
            label="Password"
            type="password"
            required
          />
        </v-card-text>

        <v-row align="center" justify="center" class="no-gutters">
          <v-btn
            class="pb-15 pt-6"
            variant="plain"
            color="secondaryBlue"
            style="font-size: 12px"
            @click="page = 2"
            >Forgot Password?</v-btn
          >
        </v-row>
        <v-card-actions class="justify-center">
          <v-col cols="auto" class="mt-10">
            <v-row align="center" justify="center">
              <v-btn variant="flat" class="bg-primaryRed" size="large" @click="submitForm">
                <v-progress-circular
                  v-if="loading"
                  indeterminate
                  size="24"
                  color="white"
                ></v-progress-circular>
                <span v-else>Login</span>
              </v-btn>
            </v-row>

            <v-row align="center" justify="center" class="mt-4">
              <p>
                or
                <v-btn
                  variant="plain"
                  color="secondaryBlue"
                  style="font-size: 12px"
                  @click="modalStore.register"
                >
                  Register
                </v-btn>
              </p>
            </v-row>
          </v-col>
        </v-card-actions>
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
          <v-text-field
            class="pb-0 mb-0"
            bg-color="#FFFFFF"
            v-model="form.email"
            :rules="[required]"
            @focus="errors.email = ''"
            :error-messages="errors.email"
            label="Email"
            clearable
            required
          />
        </v-card-text>
        <v-card-actions class="justify-center mb-5">
          <v-btn variant="flat" class="bg-primaryRed" @click="emailUser">
            <v-progress-circular
              v-if="loading"
              indeterminate
              size="24"
              color="white"
            ></v-progress-circular>
            <span v-else>Send Email</span>
          </v-btn>
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
          <v-text-field
            class="pb-0 mb-0"
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
          <v-btn variant="flat" class="mx-2" rounded="lg" color="primaryRed" @click="submitToken">
            <v-progress-circular
              v-if="loading"
              indeterminate
              size="24"
              color="white"
            ></v-progress-circular>
            <span v-else>Submit</span>
          </v-btn>
        </v-card-actions>
      </div>
      <div v-else-if="page === 4" class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center">
            <v-card-title class="text-center text-h4 pb-2 pt-5">Create New Password</v-card-title>
          </v-row>
        </v-col>
        <v-card-text>
          <v-text-field
            class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required]"
            :error-messages="errors.newPassword"
            @focus="errors.newPassword = ''"
            v-model="form.newPassword"
            label="Password"
            type="password"
            clearable
            required
          />
          <v-text-field
            class="pb-0 mb-0"
            bg-color="#FFFFFF"
            :rules="[required]"
            v-model="form.confirmPassword"
            label="Confirm Password"
            type="password"
            clearable
            required
          />
        </v-card-text>
        <v-card-actions class="justify-center mb-5">
          <v-btn
            variant="flat"
            class="mx-2"
            rounded="lg"
            color="primaryRed"
            @click="submitNewPassword"
            >Done</v-btn
          >
        </v-card-actions>
      </div>
      <div v-else class="bg-backgroundGrey">
        <v-col cols="auto">
          <v-row justify="center">
            <v-card-title class="text-center text-h4 pb-2 pt-5">Success!</v-card-title>
            <v-card-subtitle class="text-center text-subtitle-1 pb-10"
              >Your password was changed successfully</v-card-subtitle
            >
          </v-row>
        </v-col>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import { useUserStore } from '@/stores/user'
import { AxiosError } from 'axios'
import { useModalStore } from '@/stores/modal'
import { notify } from '@kyvg/vue3-notification'

const userStore = useUserStore()
const modalStore = useModalStore()
const page = ref<1 | 2 | 3 | 4 | 5>(1)
const isFullscreen = ref(false)
const loading = ref(false)

const form = ref({
  email: '',
  token: '',
  newPassword: '',
  confirmPassword: ''
})

const errors = ref({
  login: '',
  email: '',
  token: '',
  newPassword: ''
})
const required = (v: string) => !!v || 'Field is required'

const isEmail = (candidate: string) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(candidate)

const submitForm = async () => {
  loading.value = true
  if (await userStore.login(modalStore.username, modalStore.password)) {
    notify({
      title: 'Login',
      type: 'success',
      text: 'Login Success'
    })
    modalStore.close()
  } else {
    errors.value.login = 'Your username or password is incorrect'
    notify({
      title: 'Login',
      type: 'error',
      text: errors.value.login
    })
  }
  loading.value = false
}

async function emailUser() {
  if (isEmail(form.value.email)) {
    try {
      if ((await userStore.sendResetEmail(form.value.email)) === 200) {
        errors.value.email = ''
        page.value = 3
        notify({
          title: 'Reset Email',
          type: 'success',
          text: `Reset email sent`
        })
      }
    } catch (error: AxiosError | any) {
      if (error instanceof AxiosError && error.response && error.response.status === 400) {
        notify({
          title: 'Reset Email',
          type: 'error',
          text: error.response.data
        })
      }
    }
  } else {
    errors.value.email = 'Email is invalid'
    notify({
      title: 'Reset Email',
      type: 'error',
      text: errors.value.email
    })
  }
}

async function submitToken() {
  loading.value = true
  try {
    let status = await userStore.submitResetToken(form.value.token)
    if (status === 200) {
      notify({
        title: 'Reset Token',
        type: 'success',
        text: 'Reset Token Sent'
      })
      errors.value.token = ''
      page.value = 4
    }
  } catch (error: AxiosError | any) {
    if (error instanceof AxiosError && error.response && error.response.status === 400) {
      errors.value.token = 'Invalid token'
      notify({
        title: 'Reset Token',
        type: 'error',
        text: errors.value.token
      })
    }
  }
  loading.value = false
}
async function submitNewPassword() {
  if (form.value.newPassword === form.value.confirmPassword) {
    try {
      let status = await userStore.submitNewPassword(form.value.token, form.value.newPassword)
      if (status === 200) {
        errors.value.newPassword = ''
        page.value = 5
        notify({
          title: 'New Password',
          type: 'success',
          text: 'New Password Has Been Submitted'
        })
      }
    } catch (error: AxiosError | any) {
      if (error instanceof AxiosError && error.response && error.response.status === 400) {
        errors.value.newPassword = error.response.data.password
        notify({
          title: 'New Password',
          type: 'error',
          text: error.response.data.password
        })
      }
    }
  } else {
    errors.value.newPassword = 'Passwords do not match'
  }
}

watchEffect(async () => {
  const updateFullscreen = async () => {
    isFullscreen.value = window.innerWidth <= 500
  }

  await updateFullscreen()

  window.addEventListener('resize', updateFullscreen)
  return () => {
    window.removeEventListener('resize', updateFullscreen)
  }
})
</script>
