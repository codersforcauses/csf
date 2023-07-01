<script setup lang="ts">
import { ref } from 'vue'
import PopupDialog from '../components/PopupDialog.vue'

const popup = ref(false)
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/login">Login</RouterLink>
    <RouterLink to="/signup">signup</RouterLink>
    <PopupDialog />
  </nav>
  <v-button @click="popup = !popup">Popup</v-button>
</template>
