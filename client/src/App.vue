<template>
  <v-app>
    <!-- nav bars...etc -->
    <v-main> 
      <RouterView />
    </v-main>
  </v-app>
</template>
<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
export default {
  setup() {
    return{

    }
  }
}
</script>

