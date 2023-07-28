<template>
  <v-dialog v-model="value" :fullscreen="isFullscreen" width="500px">
    <v-card height="600px" class="bg-backgroundGrey">
      <div style="height: 10px">
        <v-img src="/images/Footer-min.jpeg" width="100%" alt="red background" cover />
      </div>
      <div class="d-flex justify-end">
        <v-btn variant="text" @click="$emit('update:modelValue', !modelValue)">
          <v-icon icon="mdi-close" />
        </v-btn>
      </div>
      <v-spacer />
      <v-form v-model="form">
        <v-container class="px-8">
          <v-row align="center">
            <v-col align="center">
              <v-card-title class="mx-auto text-h5 justify-center">Add Mileage</v-card-title>
              <v-card-subtitle class="mx-auto justify-center"
                >Let us know how far you travelled today!</v-card-subtitle
              >
            </v-col>
          </v-row>
          <v-row>
            <v-card-text>
              <v-row>
                <v-col>
                  <v-text-field
                    type="date"
                    label="Date"
                    v-model="mileage.date"
                    bg-color="white"
                    :max="maxDate"
                    :min="minDate"
                    :rules="[required]"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <p class="px-2 text-subtitle-2">Distance</p>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div
                    v-if="userStore.user!.travelMethod === 'RUNNING'"
                    class="ma-0 pa-0"
                    id="runner"
                  >
                    <v-slider
                      v-model="mileage.kilometres"
                      color="secondaryGreen"
                      :thumb-size="40"
                      elevation="0"
                      :step="1"
                      min="1"
                      max="50"
                    />
                  </div>
                  <div
                    v-if="userStore.user!.travelMethod === 'WALKING'"
                    id="walker"
                    class="ma-0 pa-0"
                  >
                    <v-slider
                      v-model="mileage.kilometres"
                      color="green"
                      :thumb-size="40"
                      elevation="0"
                      :step="1"
                      min="1"
                      max="50"
                    />
                  </div>
                  <div
                    v-if="userStore.user!.travelMethod === 'WHEELING'"
                    id="wheeler"
                    class="ma-0 pa-0"
                  >
                    <v-slider
                      v-model="mileage.kilometres"
                      color="green"
                      :thumb-size="40"
                      elevation="0"
                      :step="1"
                      min="1"
                      max="50"
                    />
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col align="center">
                  <v-chip class="px-6 text-h5 rounded" color="green">{{
                    mileage.kilometres
                  }}</v-chip>
                  <p class="text-subtitle-2">KILOMETERS</p>
                </v-col>
              </v-row>
            </v-card-text>
          </v-row>
        </v-container>
        <v-card-actions class="d-flex justify-center">
          <v-btn @click="handleSubmit" :disabled="!form" color="primaryRed" variant="elevated">
            <v-progress-circular
              v-if="loading"
              indeterminate
              size="24"
              color="white"
            ></v-progress-circular>
            <span v-else>ADD</span>
          </v-btn>
        </v-card-actions>
      </v-form>
      <v-spacer />
      <v-spacer />
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { ref, watchEffect } from 'vue'
import { useUserStore } from '../stores/user'
import { useMileageStore } from '@/stores/mileage'

const userStore = useUserStore()
const mileageStore = useMileageStore()
const loading = ref(false)
const isFullscreen = ref(false)
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue', 'handleSubmit'])

const mileage = ref({ kilometres: '1', date: '' })

const maxDate = ref('')
const minDate = ref('')
setMinAndMaxDate()

const form = ref(false)
const required = (v: string) => {
  return !!v || 'Field is required'
}

const value = computed({
  get() {
    return props.modelValue
  },
  set(value) {
    emit('update:modelValue', value)
  }
})

const handleSubmit = async () => {
  loading.value = true
  await mileageStore.addMileage({
    user: userStore.user!.id,
    kilometres: parseFloat(mileage.value.kilometres),
    date: mileage.value.date
  })
  emit('update:modelValue', false)
  emit('handleSubmit')
  loading.value = false
}

function setMinAndMaxDate() {
  let now = new Date()
  // need to shift, since toJSON() will get the UTC time
  let nowShifted = new Date(now.getTime() - now.getTimezoneOffset() * 60000)
  maxDate.value = nowShifted.toJSON().slice(0, 10)
  nowShifted.setDate(nowShifted.getDate() - 30)
  minDate.value = nowShifted.toJSON().slice(0, 10)
}

// Copied from SignUpModal
watchEffect(async () => {
  const updateFullscreen = async () => {
    isFullscreen.value = window.innerWidth <= 500 // Adjust the breakpoint as needed
  }

  // Initial update
  await updateFullscreen()

  // Add window resize event listener
  window.addEventListener('resize', updateFullscreen)

  // Cleanup: Remove window resize event listener
  return () => {
    window.removeEventListener('resize', updateFullscreen)
  }
})
</script>

<style scoped>
#runner :deep(.v-slider-thumb__surface) {
  border-radius: 0% !important;
  background-color: transparent !important;
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>run-fast</title><path d="M16.5,5.5A2,2 0 0,0 18.5,3.5A2,2 0 0,0 16.5,1.5A2,2 0 0,0 14.5,3.5A2,2 0 0,0 16.5,5.5M12.9,19.4L13.9,15L16,17V23H18V15.5L15.9,13.5L16.5,10.5C17.89,12.09 19.89,13 22,13V11C20.24,11.03 18.6,10.11 17.7,8.6L16.7,7C16.34,6.4 15.7,6 15,6C14.7,6 14.5,6.1 14.2,6.1L9,8.3V13H11V9.6L12.8,8.9L11.2,17L6.3,16L5.9,18L12.9,19.4M4,9A1,1 0 0,1 3,8A1,1 0 0,1 4,7H7V9H4M5,5A1,1 0 0,1 4,4A1,1 0 0,1 5,3H10V5H5M3,13A1,1 0 0,1 2,12A1,1 0 0,1 3,11H7V13H3Z" /></svg>');
  background-size: cover;
}

#walker :deep(.v-slider-thumb__surface) {
  border-radius: 0% !important;
  background-color: transparent !important;
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>walk</title><path d="M14.12,10H19V8.2H15.38L13.38,4.87C13.08,4.37 12.54,4.03 11.92,4.03C11.74,4.03 11.58,4.06 11.42,4.11L6,5.8V11H7.8V7.33L9.91,6.67L6,22H7.8L10.67,13.89L13,17V22H14.8V15.59L12.31,11.05L13.04,8.18M14,3.8C15,3.8 15.8,3 15.8,2C15.8,1 15,0.2 14,0.2C13,0.2 12.2,1 12.2,2C12.2,3 13,3.8 14,3.8Z" /></svg>');
  background-size: cover;
}

#wheeler :deep(.v-slider-thumb__surface) {
  border-radius: 0% !important;
  background-color: transparent !important;
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>wheelchair-accessibility</title><path d="M18.4,11.2L14.3,11.4L16.6,8.8C16.8,8.5 16.9,8 16.8,7.5C16.7,7.2 16.6,6.9 16.3,6.7L10.9,3.5C10.5,3.2 9.9,3.3 9.5,3.6L6.8,6.1C6.3,6.6 6.2,7.3 6.7,7.8C7.1,8.3 7.9,8.3 8.4,7.9L10.4,6.1L12.3,7.2L8.1,11.5C8,11.6 8,11.7 7.9,11.7C7.4,11.9 6.9,12.1 6.5,12.4L8,13.9C8.5,13.7 9,13.5 9.5,13.5C11.4,13.5 13,15.1 13,17C13,17.6 12.9,18.1 12.6,18.5L14.1,20C14.7,19.1 15,18.1 15,17C15,15.8 14.6,14.6 13.9,13.7L17.2,13.4L17,18.2C16.9,18.9 17.4,19.4 18.1,19.5H18.2C18.8,19.5 19.3,19 19.4,18.4L19.6,12.5C19.6,12.2 19.5,11.8 19.3,11.6C19,11.3 18.7,11.2 18.4,11.2M18,5.5A2,2 0 0,0 20,3.5A2,2 0 0,0 18,1.5A2,2 0 0,0 16,3.5A2,2 0 0,0 18,5.5M12.5,21.6C11.6,22.2 10.6,22.5 9.5,22.5C6.5,22.5 4,20 4,17C4,15.9 4.3,14.9 4.9,14L6.4,15.5C6.2,16 6,16.5 6,17C6,18.9 7.6,20.5 9.5,20.5C10.1,20.5 10.6,20.4 11,20.1L12.5,21.6Z" /></svg>');
  background-size: cover;
}

:deep().v-slider-thumb__surface::before {
  width: 0%;
  height: 0%;
}

:deep().v-slider-thumb__ripple {
  width: 50px;
  height: 50px;
  top: -5px;
  left: -5px;
}
</style>
