<template>
  <v-dialog v-model="modalStore.isRegister" :fullscreen="isFullscreen" max-width="500px">
    <v-card style="height: 100%">
      <div v-if="firstPage">
        <form class="bg-backgroundGrey">
          <v-container class="pa-0">
            <v-img :src="FooterBanner" width="100%" height="10" cover></v-img>
          </v-container>
          <v-row justify="end">
            <v-col cols="auto">
              <v-btn variant="text" @click="modalStore.close">
                <v-icon icon="mdi-close" size="32px"></v-icon
              ></v-btn>
            </v-col>
          </v-row>
          <v-card-title class="d-flex justify-center">
            <v-card flat color="backgroundGrey">
              <v-card-item>
                <v-card-title class="text-center text-h4 pb-2">Register</v-card-title>
                <v-card-subtitle class="text-center text-subtitle-1"
                  >Create an account</v-card-subtitle
                >
              </v-card-item>
            </v-card>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row dense>
                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.username"
                    label="Username"
                    :error-messages="errors.username"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.firstName"
                    label="First name"
                    :error-messages="errors.firstName"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.lastName"
                    :error-messages="errors.lastName"
                    label="Last name"
                  ></v-text-field>
                </v-col>

                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.email"
                    label="Email"
                    :error-messages="errors.email"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.password"
                    label="Password"
                    :error-messages="errors.password"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    bg-color="#FFFFFF"
                    :rules="[required]"
                    v-model="state.confirmPassword"
                    :error-messages="errors.confirmPassword"
                    label="Confirm Password"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-container>
              <v-row align="center" justify="center">
                <v-col cols="auto">
                  <v-btn
                    variant="flat"
                    rounded="lg"
                    color="primaryRed"
                    @click="
                      () => {
                        firstPage = false
                      }
                    "
                  >
                    NEXT
                  </v-btn>
                </v-col>
              </v-row>
              <v-row align="center" justify="center">
                <v-col cols="auto">
                  <v-btn
                    variant="text"
                    color="secondaryBlue"
                    style="font-size: 12px"
                    @click="modalStore.login"
                    >Already Have an account?</v-btn
                  >
                </v-col>
              </v-row>
            </v-container>
          </v-card-actions>
        </form>
      </div>
      <div v-if="!firstPage">
        <form style="bottom: auto" class="bg-backgroundGrey" @submit.prevent="">
          <v-container class="pa-0">
            <v-img
              src="/images/Footer-min.jpeg"
              width="auto"
              height="10"
              alt="red background"
              cover
            ></v-img>
          </v-container>
          <v-row justify="end">
            <v-col cols="auto">
              <v-btn variant="text" @click="modalStore.close">
                <v-icon icon="mdi-close" size="32px"></v-icon
              ></v-btn>
            </v-col>
          </v-row>
          <v-card-title class="d-flex justify-center">
            <v-card class="" flat color="backgroundGrey">
              <v-card-item>
                <v-card-title class="text-center text-h4 pb-2">Register</v-card-title>
                <v-card-subtitle class="text-center text-subtitle-1"
                  >Create an account</v-card-subtitle
                >
              </v-card-item>
            </v-card>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <p>Select an avatar</p>
                </v-col>
                <v-row dense class="px-10">
                  <v-col v-for="avatar in avatarPaths" :key="avatar.url" cols="4">
                    <v-hover v-slot:default="{ isHovering, props }">
                      <div v-bind="props" class="text-center py-3">
                        <v-avatar
                          size="70"
                          @click="selectAvatar(avatar.url)"
                          :class="{
                            'avatar-selected': avatar.isSelected === true,
                            'avatar-hovered': isHovering === true
                          }"
                        >
                          <v-img :src="`/avatars/${avatar.url}`" :alt="avatar.alt"></v-img>
                        </v-avatar>
                      </div>
                    </v-hover>
                  </v-col>
                </v-row>
                <v-col cols="12">
                  <p class="pt-5">Select main method of travel</p>
                </v-col>
                <v-row>
                  <v-container class="d-flex justify-space-evenly">
                    <div v-for="method in travelMethod" :key="method.logo" class="text-center">
                      <v-avatar
                        size="52px"
                        variant="text"
                        :class="{ 'mode-selected': method.isSelected === true }"
                        ><v-icon
                          :color="method.isSelected ? 'white' : ''"
                          size="44px"
                          :icon="method.logo"
                          @click="
                            () => {
                              selectMode(method.mode)
                            }
                          "
                        ></v-icon>
                      </v-avatar>
                      <p>{{ method.mode }}</p>
                    </div>
                  </v-container>
                </v-row>
                <v-row no-gutters class="px-2 pt-4">
                  <v-col cols="12">
                    <v-checkbox
                      density="default"
                      v-model="state.teamSignup"
                      label="I am signing up on behalf of a class"
                    ></v-checkbox>
                  </v-col>
                  <v-col cols="12">
                    <v-checkbox
                      density="default"
                      v-model="state.hasConsent"
                      label="I give consent for my data to be used by CSF"
                    ></v-checkbox>
                    <p class="text-caption px-4">
                      For more information please view
                      <span style="text-decoration: underline" class="text-secondaryBlue"
                        ><a @click="openConsentModal">our privacy statement</a></span
                      >
                    </p>
                  </v-col>
                </v-row>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-container>
              <v-row align="center" justify="center">
                <v-col cols="auto">
                  <v-btn variant="text" class="mx-2" @click="firstPage = true">BACK</v-btn>
                  <v-btn
                    variant="flat"
                    class="mx-2"
                    rounded="lg"
                    color="primaryRed"
                    @click="submit"
                  >
                    <v-progress-circular
                      v-if="loading"
                      indeterminate
                      size="24"
                      color="white"
                    ></v-progress-circular>
                    <span v-else>CREATE ACCOUNT</span>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row align="center" justify="center">
                <v-col cols="auto">
                  <v-btn
                    variant="text"
                    color="secondaryBlue"
                    style="font-size: 12px"
                    @click="modalStore.login"
                    >Already Have an account?</v-btn
                  >
                </v-col>
              </v-row>
            </v-container>
          </v-card-actions>
        </form>
      </div>
    </v-card>
  </v-dialog>
  <ConsentModal
    :dialog-modal="consentModal"
    v-if="consentModal"
    @open-consent-modal="openConsentModal"
  />
</template>

<script setup lang="ts">
import { ref, reactive, watchEffect } from 'vue'
import FooterBanner from '/images/Footer-min.jpeg'
import { type Signup } from '../types/user'
import ConsentModal from './ConsentModal.vue'
import { useUserStore } from '../stores/user'
import { AxiosError } from 'axios'
import camelize from 'camelize-ts'
import { useModalStore } from '@/stores/modal'
import { storeToRefs } from 'pinia'
import { reactiveOmit } from '@vueuse/core'
import { notify } from '@kyvg/vue3-notification'
const userStore = useUserStore()
const modalStore = useModalStore()

const isFullscreen = ref(false)
const firstPage = ref<boolean>(true)
const avatarPaths = ref([
  { url: 'avatar1.jpg', alt: 'avatar1', isSelected: true },
  { url: 'avatar2.jpg', alt: 'avatar2', isSelected: false },
  { url: 'avatar3.jpg', alt: 'avatar3', isSelected: false },
  { url: 'avatar4.jpg', alt: 'avatar4', isSelected: false },
  { url: 'avatar5.jpg', alt: 'avatar5', isSelected: false },
  { url: 'avatar6.jpg', alt: 'avatar6', isSelected: false }
])
const travelMethod = ref([
  { logo: 'mdi-run-fast', mode: 'RUNNING', isSelected: true },
  { logo: 'mdi-wheelchair-accessibility', mode: 'WHEELING', isSelected: false },
  { logo: 'mdi-walk', mode: 'WALKING', isSelected: false }
])

const { username, password } = storeToRefs(modalStore)
const state = reactive({
  username,
  password,
  firstName: '',
  lastName: '',
  email: '',
  confirmPassword: '',
  teamSignup: false,
  hasConsent: true,
  avatar: '',
  travelMethod: ''
}) as Signup

const errorMsg = ref('')
const initialErrors = {
  username: [],
  firstName: [],
  lastName: [],
  email: [],
  password: [],
  confirmPassword: []
}
const errors = reactive({ ...initialErrors })

const loading = ref(false)

const submit = async () => {
  loading.value = true
  const avatar = avatarPaths.value.filter((avatar) => avatar.isSelected === true)
  const method = travelMethod.value.filter((method) => method.isSelected === true)
  state.travelMethod = method[0].mode
  state.avatar = avatar[0].url
  if (state.confirmPassword != state.password) {
    Object.assign(errors, { confirmPassword: "Passwords don't match" })
    firstPage.value = true
  } else {
    try {
      Object.assign(errors, initialErrors)
      await userStore.registerUser(reactiveOmit(state, 'confirmPassword'))
      modalStore.login()
      notify({
        title: 'Sign Up',
        type: 'success',
        text: 'Sign Up Successful'
      })
    } catch (error: AxiosError | any) {
      console.debug(error)
      if (error instanceof AxiosError && error.message) {
        errorMsg.value = error.message
        if (error.response?.status != 201) {
          const data = camelize(error.response!.data[1])
          Object.assign(errors, data)
          firstPage.value = true
        }
      } else {
        errorMsg.value = JSON.stringify(error)
      }
      notify({
        title: 'Sign Up',
        type: 'error',
        text: 'Sign Up Unsuccessful'
      })
    }
  }
  loading.value = false
}
const selectAvatar = (url: string) => {
  avatarPaths.value.forEach((avatar) => {
    avatar.isSelected = avatar.url === url
  })
  state.avatar = url
}

const selectMode = (mode: string) => {
  travelMethod.value.forEach((method) => {
    method.isSelected = method.mode === mode
  })
  state.travelMethod = mode
}

const required = (v: string) => {
  return !!v || 'Field is required'
}

const consentModal = ref<boolean>(false)
const openConsentModal = () => {
  consentModal.value = !consentModal.value
}

watchEffect(async () => {
  const updateFullscreen = async () => {
    isFullscreen.value = window.innerWidth <= 500 // Adjust the breakpoint as needed
  }

  // Initial update
  await updateFullscreen()

  // Add window resize event listener
  window.addEventListener('resize', updateFullscreen)

  // Cleanup: Remove window resize event listener
  return () => {
    window.removeEventListener('resize', updateFullscreen)
  }
})
</script>

<style scoped>
.avatar-selected {
  border: 6px solid #345e9e !important;
}

.avatar-hovered {
  cursor: pointer !important;
}

.mode-selected {
  background-color: #345e9e !important;
}
</style>
