<template>
  <div class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center" justify="center">
    <h1 class="text-md-h1 mb-md-10 mb-7 font-weight-medium" id="title">404</h1>
    <h2 class="text-md-h2 mb-md-10 mb-7 font-weight-medium">Page Not Found</h2>
    <p class="pb-5">The page you're looking for does not exist</p>
    <v-btn
      href="/"
      target="_blank"
      class="bg-primaryRed pb-14 mb-8"
      size="x-large"
      variant="flat"
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
  line-height: 1.2em;
}
</style>
