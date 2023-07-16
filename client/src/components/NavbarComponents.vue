<template>
  <v-toolbar dark app color="black" class="hidden-sm-and-down sticky-nav">
    <v-btn :width="125" :height="60" :to="homelink" :active="false">
      <v-img :width="125" :height="60" cover src="/images/CSF_Logo_WHITE.webp"></v-img>
    </v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down d-flex align-center" align="center">
      <router-link
        v-for="item in menu.slice(0, -1)"
        :key="item.title"
        :to="item.link"
        class="navbar-link text-primaryWhite mr-8"
        flat
        :exact-active-class="'active'"
        >{{ item.title }}</router-link
      >

      <a
        v-for="item in menu.slice(-1)"
        :key="item.title"
        :href="item.link"
        target="_blank"
        class="navbar-link text-primaryWhite mr-8"
        flat
        :exact-active-class="'active'"
        >{{ item.title }}</a
      >
      <v-row class="mr-5">
        <v-btn
          v-if="user"
          class="text-primaryWhite bg-transparent mr-3 pb-1"
          size="x-small"
          variant="flat"
          :style="{ fontFamily: 'Hackney', fontSize: '20px' }"
          style="letter-spacing: 0.5px"
          >{{ user.username }}</v-btn
        >

        <v-btn
          v-if="user"
          class="bg-primaryRed pb-1"
          size="x-small"
          variant="flat"
          :style="{ fontFamily: 'Hackney', fontSize: '20px' }"
          style="letter-spacing: 0.5px"
          @click="openPopupDialog"
          >LOGOUT</v-btn
        >
        <v-btn
          v-if="!user"
          class="text-primaryWhite bg-transparent mr-3 pb-1"
          size="x-small"
          variant="flat"
          :style="{ fontFamily: 'Hackney', fontSize: '20px' }"
          style="letter-spacing: 0.5px"
          @click="openLoginModal"
          >LOGIN</v-btn
        >
        <v-btn
          v-if="!user"
          class="bg-primaryRed pb-1"
          size="x-small"
          variant="flat"
          :style="{ fontFamily: 'Hackney', fontSize: '20px' }"
          style="letter-spacing: 0.5px"
          @click="openSignUpModal"
          >SIGNUP</v-btn
        >
      </v-row>
    </v-toolbar-items>
  </v-toolbar>
  <v-toolbar dark app color="black" class="hidden-md-and-up sticky-nav">
    <v-btn :width="125" :height="60" :to="homelink" :active="false">
      <v-img :width="125" :height="60" cover src="/images/CSF_Logo_WHITE.webp" />
    </v-btn>
    <v-spacer></v-spacer>
    <v-dialog
      v-model="dialog"
      :fullscreen="mobile"
      transition="dialog-up-transition"
      class="hidden-md-and-up"
    >
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" class="hidden-md-and-up">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-card color="black">
        <v-container class="pa-0 ma-0">
          <v-toolbar color="black" class="hidden-md-and-up sticky-nav">
            <v-btn :width="125" :height="60" :to="homelink" @click="dialog = false" :active="false">
              <v-img
                :width="125"
                :height="60"
                cover
                src="/images/CSF_Logo_WHITE.webp"
              />
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon @click="dialog = false" class="hidden-md-and-up">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
        </v-container>

        <v-list class="listItem pa-0 mt-16">
          <v-img
            :src="FooterBanner"
            width="100%"
            height="6"
            class="hidden-md-and-up sticky-nav-img"
            cover
          />

          <v-list-item
            v-for="(item, index) in menu.slice(0, -1)"
            :key="index"
            :value="index"
            :to="item.link"
            @click="dialog = false"
            class="mt-2"
          >
            <template v-slot:prepend>
              <v-icon v-if="item.icon">{{ item.icon }}</v-icon>
            </template>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
          <v-list-item
            v-for="(item, index) in menu.slice(-1)"
            :key="index"
            :value="index"
            :href="item.link"
            target="_blank"
            @click="dialog = false"
            class="mt-2"
          >
            <template v-slot:prepend>
              <v-icon v-if="item.icon">{{ item.icon }}</v-icon>
            </template>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
        <v-row class="ml-4 mb-6 mr-4" align="end">
          <v-icon icon="mdi-login" color="text-primaryWhite pb-6" />
          <v-spacer />
          <v-btn
            v-if="user"
            class="text-primaryWhite bg-transparent mr-3 pb-1"
            size="large"
            variant="flat"
            :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
            style="letter-spacing: 0.5px"
            >{{ user.username }}</v-btn
          >

          <v-btn
            v-if="user"
            class="bg-primaryRed"
            size="large"
            variant="flat"
            :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
            style="letter-spacing: 0.5px"
            @click="openPopupDialog"
            >LOGOUT</v-btn
          >

          <v-btn
            v-if="!user"
            class="text-primaryWhite bg-transparent mr-3 pb-1"
            size="large"
            variant="flat"
            :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
            style="letter-spacing: 0.5px"
            @click="openLoginModal"
            >LOGIN</v-btn
          >
          <v-btn
            v-if="!user"
            class="bg-primaryRed"
            size="large"
            variant="flat"
            :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
            style="letter-spacing: 0.5px"
            @click="openSignUpModal"
            >SIGNUP</v-btn
          >
        </v-row>
      </v-card>
    </v-dialog>
  </v-toolbar>

  <v-img :src="FooterBanner" width="100%" height="8" class="sticky-nav-img" cover />

  <SignUpModal
    :dialog-modal="signupModal"
    v-if="signupModal"
    @open-signUp-modal="openSignUpModal"
  />

  <LoginModal :dialog-modal="loginModal" v-if="loginModal" @open-login-modal="openLoginModal" />

  <PopupDialog
    v-model="openConfirmLogoutDialogueBox"
    title="Confirm Logout"
    text="Are you sure you want to logout of your account?"
    submitText="Logout"
    @handle-submit="logout"
  />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import SignUpModal from './SignUpModal.vue'
import FooterBanner from '/images/Footer-min.webp'
import LoginModal from './LoginModal.vue'
import PopupDialog from './PopupDialog.vue'

import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'
import router from '@/router'

const userStore = useUserStore()

const { user } = storeToRefs(userStore)

const { mobile } = useDisplay()
const dialog = ref<boolean>(false)
const signupModal = ref<boolean>(false)
const loginModal = ref<boolean>(false)
const openConfirmLogoutDialogueBox = ref<boolean>(false)

let homelink = '/'

const openSignUpModal = () => {
  signupModal.value = !signupModal.value
}

const openLoginModal = () => {
  loginModal.value = !loginModal.value
}

const openPopupDialog = () => {
  openConfirmLogoutDialogueBox.value = true
}

const logout = () => {
  userStore.logout()
  router.push(homelink)
}

const menu = [
  { icon: 'mdi-card-account-details-outline', title: 'About', link: '/' },
  { icon: 'mdi-chart-bar', title: 'Dashboard', link: '/dashboard' },
  { icon: 'mdi-account-group', title: 'Team', link: '/team' },
  { icon: 'mdi-calendar', title: 'Events', link: '/events' },
  { icon: 'mdi-trophy', title: 'Challenges', link: '/challenges' },
  { icon: 'mdi-star', title: 'Leaderboards', link: '/' },
  { icon: 'mdi-currency-usd', title: 'Donate', link: 'https://stride-for-education.raisely.com' }
]
</script>

<style>
.listItem {
  color: white;
  background-color: black;
}

.sticky-nav {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 999;
}

.sticky-nav-img {
  position: fixed;
  top: 60;
  width: 100%;
  z-index: 999;
}

.navbar-link {
  text-decoration: none;
  font-size: 14px;
  font-weight: bold;
}

.navbar-link:hover,
.navbar-link.active {
  position: relative;
}

.navbar-link:hover::after,
.navbar-link.active::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -5px;
  width: 100%;
  height: 2px;
  background-color: #ed1c24;
}
</style>
