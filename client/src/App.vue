<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <v-app>
    <!-- nav bars...etc -->
    <v-main> 
      <RouterView />
    </v-main>
  </v-app>
</template>

