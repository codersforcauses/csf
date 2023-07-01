<script setup lang="ts">
import { ref } from 'vue'
import PopupDialog from '../components/PopupDialog.vue'
import { fa } from 'vuetify/locale'

const popup = ref(false)
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/login">Login</RouterLink>
    <RouterLink to="/signup">signup</RouterLink>
  </nav>
  <v-button @click="popup = !popup" @close="popup = false">
    <PopupDialog :popup="popup" />
    Popup
  </v-button>
</template>
