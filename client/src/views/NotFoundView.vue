<template>
  <div class="ma-0 px-4 pt-4 pb-0 text-center flex align-center justify-center">
    <h1 class="mb-md-3 font-weight-medium" id="title">404</h1>
    <h2 class="text-h4 text-md-h3 mb-md-5 mb-3 font-weight-medium">Page Not Found</h2>
    <p class="pb-5 pb-md-7">The page you're looking for does not exist.</p>
    <v-btn
      href="/"
      target="_blank"
      class="text-primaryWhite bg-primaryRed mr-3 pb-1"
      size="large"
      :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
      style="letter-spacing: 0.5px"
    >
      Return Home
    </v-btn>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
#title {
  font-family: 'Hackney' !important;
  font-size: 7em;
  color: black;
}
</style>
