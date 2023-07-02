<template>
  <v-toolbar dark app color="black" class="hidden-sm-and-down">
    <v-img
      src="/images/CSF_Logo_WHITE.png"
      width="125"
      height="60"
      max-width="125"
      max-height="60"
    ></v-img>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn v-for="item in menu" :key="item.title" :to="item.link" flat>{{ item.title }}</v-btn>
      <v-btn active @click="openLoginModal">LOGIN</v-btn>
      <v-btn active @click="openSignUpModal">SIGNUP</v-btn>
    </v-toolbar-items>
  </v-toolbar>
  <v-toolbar dark app color="black" class="hidden-md-and-up">
    <v-img
      src="/images/CSF_Logo_WHITE.png"
      width="125"
      height="60"
      max-width="125"
      max-height="60"
    ></v-img>
    <v-spacer></v-spacer>
    <v-dialog
      v-model="dialog"
      :fullscreen="mobile"
      transition="dialog-up-transition"
      class="hidden-md-and-up"
    >
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" class="hidden-md-and-up pr-3">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-card color="black">
        <v-container class="pa-0 ma-0">
          <v-toolbar dark app color="black" class="hidden-md-and-up">
            <v-img
              src="/images/CSF_Logo_WHITE.png"
              width="125"
              height="60"
              max-width="125"
              max-height="60"
            ></v-img>
            <v-spacer></v-spacer>
            <v-btn icon @click="dialog = false" class="hidden-md-and-up pr-3">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
        </v-container>
        <v-container class="pa-0">
          <v-img
            src="/images/Footer-min.jpeg"
            width="100%"
            height="8"
            class="hidden-md-and-up"
            cover
          ></v-img>
        </v-container>
        <v-list class="listItem pa-0">
          <v-list-item
            v-for="(item, index) in menu"
            :key="index"
            :value="index"
            :to="item.link"
            @click="dialog = false"
          >
            <template v-slot:prepend>
              <v-icon v-if="item.icon">{{ item.icon }}</v-icon>
            </template>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
          <v-list-item @click="openLoginModal" variant="tonal">
            <template v-slot:prepend>
              <v-icon style="color: #fff; opacity: 1" icon="mdi-login"></v-icon>
            </template>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
          <v-list-item @click="openSignUpModal" variant="tonal">
            <template v-slot:prepend>
              <v-icon style="color: #fff; opacity: 1" icon="mdi-pencil-box"></v-icon>
            </template>
            <v-list-item-title>Sign Up</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </v-toolbar>
  <v-img src="/images/Footer-min.jpeg" width="100%" height="8" cover></v-img>

  <SignUpModal
    :dialog-modal="signupModal"
    v-if="signupModal"
    @open-signUp-modal="openSignUpModal"
  />

  <LoginModalVue :dialog-modal="loginModal" v-if="loginModal" @open-signUp-modal="openLoginModal" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import SignUpModal from './SignUpModal.vue'
import LoginModalVue from './LoginModal.vue'

const { mobile } = useDisplay()
const dialog = ref<boolean>(false)
const signupModal = ref<boolean>(false)
const loginModal = ref<boolean>(false)

const openSignUpModal = () => {
  signupModal.value = !signupModal.value
}

const openLoginModal = () => {
  loginModal.value = !loginModal.value
}

const menu = [
  { icon: 'mdi-card-account-details-outline', title: 'About Us', link: '/' },
  { icon: 'mdi-chart-bar', title: 'Dashboard', link: '/' },
  { icon: 'mdi-trophy', title: 'Challenges', link: '/' },
  { icon: 'mdi-account-group', title: 'Team Page', link: '/' },
  { icon: 'mdi-calendar', title: 'Events', link: '/' },
  { icon: 'mdi-star', title: 'Leaderboards', link: '/' },
]
</script>

<style>
.listItem {
  color: white;
  background-color: black;
}
</style>
