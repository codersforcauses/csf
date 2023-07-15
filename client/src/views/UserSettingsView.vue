<template>
  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-text-field bg-color="#FFFFFF" v-model="state.username" label="Username"></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field
          bg-color="#FFFFFF"
          v-model="state.firstName"
          label="First name"
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field bg-color="#FFFFFF" v-model="state.lastName" label="Last name"></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field bg-color="#FFFFFF" v-model="state.email" label="Email"></v-text-field>
      </v-col>
    </v-row>
    <v-col cols="12">
      <p>Select an Avatar</p>
    </v-col>
    <v-row dense class="px-10">
      <v-col v-for="avatar in avatarPaths" :key="avatar.url" cols="4">
        <div class="text-center py-3">
          <v-avatar
            size="70"
            @click="selectAvatar(avatar.url)"
            :class="{ 'avatar-selected': avatar.isSelected === true }"
          >
            <v-img :src="`/avatars/${avatar.url}`" :alt="avatar.alt"></v-img>
          </v-avatar>
        </div>
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
    <v-row>
      <v-btn class="bg-primaryRed ma-4" @click="null">Update </v-btn>
    </v-row>
    <v-row>
      <v-btn class="bg-primaryRed ma-4" @click="showChangePasswordModal = true"
        >Change Password
      </v-btn>
      <ChangePasswordModal
        v-if="showChangePasswordModal"
        v-model="showChangePasswordModal"
        @close="showChangePasswordModal = false"
        @success="passwordChanged"
      />
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import ChangePasswordModal from '../components/ChangePasswordModal.vue'
import { ref, reactive } from 'vue'
import { useUserStore } from '../stores/user'
import { type UserSettings } from '../types/user'

const userStore = useUserStore()

const state = reactive<UserSettings>({
  username: '',
  firstName: '',
  lastName: '',
  email: '',
  avatar: '',
  travelMethod: ''
})

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

const selectAvatar = (url: string) => {
  avatarPaths.value.forEach((avatar) => {
    avatar.isSelected = avatar.url === url ? !avatar.isSelected : false
  })
  state.avatar = url
}

const selectMode = (mode: string) => {
  travelMethod.value.forEach((method) => {
    method.isSelected = method.mode === mode ? !method.isSelected : false
  })
  state.travelMethod = mode
}

const showChangePasswordModal = ref(false)
const showSuccessDialog = ref(false)

function passwordChanged() {
  showChangePasswordModal.value = false
  showSuccessDialog.value = true
}
</script>
