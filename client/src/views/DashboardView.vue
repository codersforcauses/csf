<template>
  <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center" justify="center">
    <h1>Welcome back, {{ tempUserFirstName }}!</h1>
  </v-row>
  <v-divider />
  <v-row class="ma-0 pl-4 pr-4 pb-0 pt-0" align="center">
    <v-col>
      <v-card variant="flat" class="pb-1">
        <v-container class="pa-0" fluid>
          <v-row class="ma-0">
            <v-col cols="auto" class="pl-0 pr-0">
              <v-icon icon="mdi-run-fast" size="52" />
            </v-col>
            <v-col>
              <v-chip color="green" class="rounded text-h5">{{ tempUserMileage }} KM</v-chip>
              <v-card-subtitle>TOTAL</v-card-subtitle>
            </v-col>
            <v-spacer />
            <v-col cols="auto">
              <v-btn
                variant="elevated"
                elevated="2"
                :ripple="true"
                icon="mdi-plus"
                color="primaryRed"
                @click="dialog = true"
              />
              <MileageModal v-model="dialog" />
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
  <v-divider />
  <v-row class="ma-0 px-4 pt-0 pb-0" align="center">
    <v-col>
      <h2>Daily KMs</h2>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MileageModal from '../components/MileageModal.vue'

const tempUserFirstName = ref('John')
const tempUserMileage = ref(100)
const dialog = ref(false)
</script>

<style scoped></style>
