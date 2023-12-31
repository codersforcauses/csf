<template>
  <v-container>
    <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center" justify="center">
      <h1 class="text-center">Settings</h1>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-text-field
          bg-color="#FFFFFF"
          v-model="state.username"
          label="Username"
          :error-messages="errors.username"
          @focus="errors.username = ''"
        />
      </v-col>
      <v-col cols="12">
        <v-text-field
          bg-color="#FFFFFF"
          v-model="state.firstName"
          label="First name"
          :error-messages="errors.firstName"
          @focus="errors.firstName = ''"
        />
      </v-col>
      <v-col cols="12">
        <v-text-field
          bg-color="#FFFFFF"
          v-model="state.lastName"
          label="Last name"
          :error-messages="errors.lastName"
          @focus="errors.lastName = ''"
        />
      </v-col>
      <v-col cols="12">
        <v-text-field
          bg-color="#FFFFFF"
          v-model="state.email"
          :error-messages="errors.email"
          @focus="errors.email = ''"
          label="Email"
        />
      </v-col>
    </v-row>
    <v-col cols="12">
      <p>Change avatar</p>
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
              <v-img :src="`/avatars/${avatar.url}`" :alt="avatar.alt" />
            </v-avatar>
          </div>
        </v-hover>
      </v-col>
    </v-row>
    <v-col cols="12">
      <p class="pt-5">Change main method of travel</p>
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
            />
          </v-avatar>
          <p>{{ method.mode }}</p>
        </div>
      </v-container>
    </v-row>
    <v-row>
      <v-btn class="bg-primaryRed ma-4" @click="changeDetails">
        <v-progress-circular
          v-if="loading"
          indeterminate
          size="24"
          color="white"
        ></v-progress-circular>
        <span v-else>Update</span>
      </v-btn>
      <v-spacer />
      <v-btn class="bg-primaryRed ma-4" @click="showChangePasswordModal = true"
        >Change Password
      </v-btn>
    </v-row>
  </v-container>
  <ChangePasswordModal
    v-if="showChangePasswordModal"
    v-model="showChangePasswordModal"
    @close="showChangePasswordModal = false"
    @success="passwordChanged"
  />
</template>

<script setup lang="ts">
import ChangePasswordModal from '../components/ChangePasswordModal.vue'
import { ref, reactive } from 'vue'
import { useUserStore } from '../stores/user'
import { type UserSettings, type ChangeDetailsError } from '../types/user'
import { AxiosError } from 'axios'
import camelize from 'camelize-ts'
import { notify } from '@kyvg/vue3-notification'

const userStore = useUserStore()
const loading = ref(false)

const state = reactive<UserSettings>({
  username: userStore.user!.username,
  firstName: userStore.user!.firstName,
  lastName: userStore.user!.lastName,
  email: userStore.user!.email,
  avatar: userStore.user!.avatar,
  travelMethod: userStore.user!.travelMethod
})

const errors = reactive<ChangeDetailsError>({
  username: '',
  email: '',
  firstName: '',
  lastName: ''
})

const avatarPaths = ref(
  Array(6)
    .fill(0)
    .map((e, i) => {
      return {
        url: `avatar${i + 1}.jpg`,
        alt: `avatar${i + 1}`,
        isSelected: state.avatar === `avatar${i + 1}.jpg`
      }
    })
)

const travelMethod = ref([
  { logo: 'mdi-run-fast', mode: 'RUNNING', isSelected: state.travelMethod === 'RUNNING' },
  {
    logo: 'mdi-wheelchair-accessibility',
    mode: 'WHEELING',
    isSelected: state.travelMethod === 'WHEELING'
  },
  { logo: 'mdi-walk', mode: 'WALKING', isSelected: state.travelMethod === 'WALKING' }
])

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

const showChangePasswordModal = ref(false)
const showSuccessDialog = ref(false)

async function changeDetails() {
  loading.value = true
  try {
    let status = await userStore.changeDetails(state)
    if (status === 200) {
      // update the user details in the store
      userStore.getUser()
      // TODO: replace this with a proper dialog/alert
      notify({
        title: 'Change User Details',
        type: 'success',
        text: 'Details Successfully Changed'
      })
    }
  } catch (error: AxiosError | any) {
    if (error instanceof AxiosError && error.response && error.response.status === 400) {
      let newErrors = camelize(error.response.data) as ChangeDetailsError
      Object.assign(errors, newErrors)
      notify({
        title: 'Change User Details',
        type: 'error',
        text: 'Error On Changing Details'
      })
    }
  }
  loading.value = false
}

function passwordChanged() {
  showChangePasswordModal.value = false
  showSuccessDialog.value = true
}
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
