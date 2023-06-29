<template>
  <v-toolbar dark app color="black" class="hidden-sm-and-down">
    <img alt="CSF Logo" src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn v-for="item in menu" :key="item.title" :to="item.link" flat>{{ item.title }}</v-btn>
    </v-toolbar-items>
  </v-toolbar>
  <v-toolbar dark app color="black" class="hidden-md-and-up">
    <img alt="CSF Logo" src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-spacer></v-spacer>
    <v-dialog
      v-model="dialog"
      :fullscreen="mobile"
      transition="dialog-up-transition"
      class="hidden-md-and-up"
    >
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" class="hidden-md-and-up menuIcon">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-card class="overall">
        <v-container class="pa-0 ma-0">
          <v-toolbar dark app color="black" class="hidden-md-and-up">
            <img alt="CSF Logo" src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
            <v-spacer></v-spacer>
            <v-btn icon @click="dialog = false" class="hidden-md-and-up menuIcon">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
        </v-container>
        <v-container class="pt-0 pl-0 pb-2 pr-0 border-container">
          <img id="app" src="@/assets/Footer-min.jpeg" class="border hidden-md-and-up" />
        </v-container>
        <v-list class="listItem">
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
        </v-list>
      </v-card>
    </v-dialog>
  </v-toolbar>
  <img id="app" src="@/assets/Footer-min.jpeg" class="border hidden-sm-and-down" />
  <img id="app" src="@/assets/Footer-min.jpeg" class="border hidden-md-and-up" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

const { mobile } = useDisplay()
const dialog = ref(false)
const menu = [
  { icon: 'mdi-card-account-details-outline', title: 'About Us', link: '/' },
  { icon: 'mdi-chart-bar', title: 'Dashboard', link: '/' },
  { icon: 'mdi-trophy', title: 'Challenges', link: '/' },
  { icon: 'mdi-account-group', title: 'Team Page', link: '/' },
  { icon: 'mdi-calendar', title: 'Events', link: '/' },
  { icon: 'mdi-star', title: 'Leaderboards', link: '/' },
  { icon: 'mdi-login', title: 'Login', link: '/' },
  { icon: 'mdi-pencil-box', title: 'Sign Up', link: '/signup' }
]
</script>

<style>
@import url('https://use.fontawesome.com/releases/v5.15.4/css/all.css');
.menuIcon {
  padding-right: 3%;
}
.listItem {
  color: white;
  background-color: black;
}
.overall {
  background-color: black;
}
.border {
  height: 100%;
  width: 100%;
  max-height: 10px;
  overflow: hidden;
  position: absolute;
}
.border-container {
  position: relative;
}
.v-list {
  padding-top: 0px;
}
</style>
