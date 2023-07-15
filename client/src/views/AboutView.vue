<template>
  <v-img :src="CSFBanner" width="100%"></v-img>
  <v-row class="pt-8 px-8 bg-secondaryGrey" no-gutters justify="center">
    <h2 class="text-secondaryTint text-center">
      <span class="font-weight-bold">Education changes lives:</span>
      we are challenging all of you to let your kilometres make a difference!
    </h2>
  </v-row>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
    <path
      fill="#202020"
      d="m0 64 60 10.7c60 10.3 180 32.3 300 48 120 16.3 240 26.3 360 16C840 128 960 96 1080 85.3c120-10.3 240-.3 300 5.4l60 5.3V0H0Z"
    />
  </svg>
  <v-img :src="StrideForEducationRBGLogoWebp" class="px-8 mt-n8 mb-8 w-100" />
  <v-divider class="mx-4" />
  <p class="pa-8">
    Community Spirit Foundation is running Stride For Education – a challenge designed to motivate
    kids across Australia to get active while learning about how our foundation supports First
    Nations young people.
  </p>
  <p class="px-8 pb-8">
    Clock as many kilometres as you can with your team or as an individual! Stay informed and
    motivated by checking the leaderboard, where you can see how your performance stacks up against
    other participants. Compare your progress with other users, teams, or even your own teammates,
    and let the friendly competition inspire you to reach new levels of achievement.
  </p>
  <v-img :src="StrideForEducationGifWebp" width="100%"></v-img>
  <p class="pa-8">
    Every step you take as part of this challenge is one step further in Community Spirit
    Foundation's journey of helping to support First Nations young people to realise their potential
    through lifelong learning.
  </p>
  <v-row justify="center" class="my-4" no-gutters>
    <v-btn
      class="bg-primaryRed pb-14 mb-8"
      size="x-large"
      variant="flat"
      :style="{ fontFamily: 'Hackney', fontSize: '42px' }"
      style="letter-spacing: -1px"
      @click="openSignUpModal"
    >
      REGISTER NOW
    </v-btn>
  </v-row>

  <v-row class="px-8 bg-secondaryBlue" no-gutters>
    <h2 class="py-2" :style="{ fontFamily: 'Hackney', fontSize: '58px' }">OUR STORY</h2>
    <v-divider class="mr-16" />
    <p class="py-5">
      Working in partnership with remote First Nations peoples to ensure their young people have the
      best outcomes and opportunities through education and lifelong learning, is the Community
      Spirit Foundation.
    </p>
  </v-row>
  <v-row class="px-8 bg-secondaryGreen" no-gutters>
    <h2 class="py-2" :style="{ fontFamily: 'Hackney', fontSize: '58px' }">OUR MISSION</h2>
    <v-divider class="mr-16" />
    <p class="py-5">
      To work alongside remote First Nations Peoples and communities to enable their young people to
      fulfil their potential.
    </p>
  </v-row>
  <v-row class="px-8 bg-primaryRed" no-gutters>
    <h2 class="py-2" :style="{ fontFamily: 'Hackney', fontSize: '58px' }">OUR BELIEFS</h2>
    <v-divider class="mr-16" />
    <v-list no-gutters class="bg-primaryRed my-3">
      <v-list-item v-for="belief in beliefs" :key="belief">
        <v-list-item-icon>
          <v-icon>mdi-circle-medium</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          {{ belief }}
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-row>
  <v-img :src="studentsLearning" width="100%"></v-img>
  <v-row class="px-8 bg-secondaryGrey text-secondaryTint" no-gutters>
    <h2 class="py-2" :style="{ fontFamily: 'Hackney', fontSize: '58px' }">DONATE TODAY</h2>
    <v-divider class="mr-16" />
    <p class="py-5">
      The vision at Community Spirit Foundation has always been ambitious but simple: An Australia
      where Indigenous and non-Indigenous children have the same education outcomes and
      opportunities in life.
    </p>
    <p class="pb-5">
      By donating to Community Spirit Foundation you will be supporting Aboriginal and Torres Strait
      Islander Children to dream big and have choices.
    </p>
    <v-row justify="center" class="my-7" no-gutters>
      <v-btn
        href="https://stride-for-education.raisely.com"
        target="_blank"
        class="bg-primaryRed pb-14 mb-6"
        size="x-large"
        :style="{ fontFamily: 'Hackney', fontSize: '42px' }"
        style="letter-spacing: -0.5px"
      >
        DONATE
      </v-btn>
    </v-row>
  </v-row>
  <v-img :src="thankYou" width="100%"></v-img>
  <v-row class="ma-8" no-gutters>
    <p>
      The Community Spirit Foundation acknowledges and pays our respects to the past, present and
      emerging traditional custodians of the land on which we work and live. Aboriginal and Torres
      Strait Islander users are advised that this website may contain images and voices of people
      who have died.
    </p></v-row
  >
  <Footer />
  <SignUpModal
    :dialog-modal="signupModal"
    v-if="signupModal"
    @open-signUp-modal="openSignUpModal"
  />
</template>

<script setup lang="ts">
import Footer from '@/components/Footer.vue'
import { ref } from 'vue'
import SignUpModal from '@/components/SignUpModal.vue'
import studentsLearning from '/images/students_learning.webp'
import thankYou from '@/assets/images/thank_you.jpg'
import StrideForEducationGifWebp from '@/assets/gif/Stride_1Webp.webp'
import CSFBanner from '@/assets/images/CSF_Banner.jpg'
import StrideForEducationRBGLogoWebp from '@/assets/images/SFE_RGB_Logo.webp'

const signupModal = ref<boolean>(false)
const openSignUpModal = () => {
  signupModal.value = !signupModal.value
}

const beliefs = [
  'Every young person we work with should be able to dream big and be proud.',
  'Building community capacity is our priority.',
  'We work to a community development approach with long term partnerships at the core.',
  'To achieve and have a life full of opportunity, we believe education is key.',
  'Education can be in many forms – formal, informal, and lifelong. Culturally responsive education is paramount.',
  'Culturally responsive education is paramount.'
]
</script>

<style></style>
