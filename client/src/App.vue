<script setup lang="ts">
import NavbarComponents from './components/NavbarComponents.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <NavbarComponents />
  </header>
  <RouterView />
</template>
