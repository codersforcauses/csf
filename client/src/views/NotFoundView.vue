<template>
  <v-container class="not-found-container pa-0" fluid fill-height>
    <v-row align="center" justify="center">
      <v-col cols="12" class="text-center">
        <h1 class="mb-md-3 font-weight-medium" id="title">404</h1>
        <h2 class="text-h4 text-md-h3 mb-md-5 mb-3 font-weight-medium">Page Not Found</h2>
        <p class="pb-5 pb-md-7">The page you're looking for does not exist.</p>
        <v-btn
          href="/"
          class="text-primaryWhite bg-primaryRed mr-3 pb-1"
          size="large"
          :style="{ fontFamily: 'Hackney', fontSize: '28px' }"
          style="letter-spacing: 0.5px"
        >
          Return Home
        </v-btn>
      </v-col>
    </v-row>
    <v-row align="end">
      <v-col cols="12">
        <v-img :src="NotFoundFooter" eager width="100%" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import NotFoundFooter from '/images/404-footer.png'
</script>

<style scoped>
#title {
  font-family: 'Hackney' !important;
  font-size: 7em;
  color: black;
}

.not-found-container {
  display: flex;
  flex-direction: column;
  min-height: 95vh;
}
</style>
