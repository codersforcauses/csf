<script setup lang="ts">
import Navbar from './components/NavBar.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <RouterView />
</template>
