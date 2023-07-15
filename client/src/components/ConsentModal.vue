<template>
  <v-dialog v-model="dialog" :fullscreen="isFullscreen" max-width="500px">
    <v-card style="height: 100%">
      <div class="bg-backgroundGrey">
        <v-card-title class="justify-center">
          <h3>Privacy Statement</h3>
        </v-card-title>
        <v-card-text>
          <p class="text--primary" align="justify">
            The primary purpose for which your Personal Information is collected for all events is
            so that it can be disclosed to the Community Spirit Foundation for the purpose of:
          </p>
          <p class="text--primary" align="justify">
            (i) conducting, administering and evaluating the 'Stride For Education' events;
          </p>
          <p class="text--primary" align="justify">
            (ii) providing individuals with services, promotional material and other information in
            relation to the 'Stride For Education' virtual events; and
          </p>
          <p class="text--primary" align="justify">
            (iii) direct marketing by the Community Spirit Foundation.
          </p>
        </v-card-text>
        <v-card-actions>
          <v-btn block @click="closeModal">Close Privacy Statement</v-btn>
        </v-card-actions>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const isFullscreen = ref(false)
const dialog = ref(true)
defineProps(['consentModal'])
const emit = defineEmits(['openConsentModal'])

const closeModal = () => {
  emit('openConsentModal', false)
}
</script>
