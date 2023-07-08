<!-- <template>
  <v-img :src="FooterBanner" height="120" cover>
    <p class="text-primaryWhite pl-3 font-weight-bold mt-2">Contact Us</p>
    <v-row align="center" no-gutters class="pl-5">
      <v-col cols="auto">
        <v-icon color="white" class="pr-3">mdi-email</v-icon>
        <a class="text-primaryWhite">admin@communityspiritfoundation.org.au</a>
      </v-col>
    </v-row>
    <v-row align="center" no-gutters class="pl-6">
      <v-icon color="white" size="small" class="pr-4">mdi-phone</v-icon>
      <p class="text-primaryWhite">(03) 9686 4813</p>
    </v-row>
    <v-row align="center" justify="end" no-gutters class="mr-1">
      <v-col cols="auto">
        <v-btn
          href="https://www.facebook.com/CommunitySpiritFoundation"
          target="_blank"
          color="white"
          variant="text"
          size="x-small"
        >
          <v-icon color="white" size="28">mdi-facebook</v-icon>
        </v-btn>
        <v-btn
          href="https://twitter.com/CommSpiritFdn"
          target="_blank"
          color="white"
          variant="text"
          size="x-small"
        >
          <v-icon color="white" size="28">mdi-twitter</v-icon>
        </v-btn>
        <v-btn
          href="https://www.linkedin.com/company/community-spirit-foundation/"
          target="_blank"
          color="white"
          variant="text"
          size="x-small"
        >
          <v-icon color="white" size="28">mdi-linkedin</v-icon>
        </v-btn>
        <v-btn
          href="https://www.youtube.com/channel/UCBwN8LGzIwiP27pamn9K9xQ"
          target="_blank"
          color="white"
          variant="text"
          size="x-small"
        >
          <v-icon color="white" size="28">mdi-youtube</v-icon>
        </v-btn>
        <v-btn
          href="https://www.instagram.com/communityspiritfoundation/"
          target="_blank"
          color="white"
          variant="text"
          size="x-small"
        >
          <v-icon color="white" size="28">mdi-instagram</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-img>
</template> -->

<template>
  <v-layout>
    <v-footer class="pa-0">
      <v-img :src="FooterBanner" height="120" cover>
        <v-row justify="end" class="mt-2 mr-1">
          <v-btn
            href="https://www.facebook.com/CommunitySpiritFoundation"
            target="_blank"
            color="white"
            variant="text"
            size="x-small"
          >
            <v-icon color="white" size="28">mdi-facebook</v-icon>
          </v-btn>
          <v-btn
            href="https://twitter.com/CommSpiritFdn"
            target="_blank"
            color="white"
            variant="text"
            size="x-small"
          >
            <v-icon color="white" size="28">mdi-twitter</v-icon>
          </v-btn>
          <v-btn
            href="https://www.linkedin.com/company/community-spirit-foundation/"
            target="_blank"
            color="white"
            variant="text"
            size="x-small"
          >
            <v-icon color="white" size="28">mdi-linkedin</v-icon>
          </v-btn>
          <v-btn
            href="https://www.youtube.com/channel/UCBwN8LGzIwiP27pamn9K9xQ"
            target="_blank"
            color="white"
            variant="text"
            size="x-small"
          >
            <v-icon color="white" size="28">mdi-youtube</v-icon>
          </v-btn>
          <v-btn
            href="https://www.instagram.com/communityspiritfoundation/"
            target="_blank"
            color="white"
            variant="text"
            size="x-small"
          >
            <v-icon color="white" size="28">mdi-instagram</v-icon>
          </v-btn>
        </v-row>
        <v-row>
          <v-col>
            <v-row>
              <p class="text-primaryWhite ml-6 font-weight-bold">Contact Us</p>
            </v-row>
            <v-row class="ml-5">
              <v-icon color="white" class="pr-3" justify="center">mdi-email</v-icon>
              <a class="text-primaryWhite">admin@communityspiritfoundation.org.au</a>
            </v-row>
            <v-row class="ml-6">
              <v-icon color="white" size="small" class="pr-3">mdi-phone</v-icon>
              <p class="text-primaryWhite">(03) 9686 4813</p>
            </v-row>
          </v-col>
        </v-row>
      </v-img>
    </v-footer>
  </v-layout>
</template>

<script setup lang="ts">
import FooterBanner from '/images/Footer-min.jpeg'
</script>
