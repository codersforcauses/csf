<template>
  <div v-if="!loading">
  <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center" justify="center">
    <h1>Welcome back, {{ firstName }}</h1>
  </v-row>
  <v-divider />
  <v-row class="ma-0 pl-4 pr-4 pb-0 pt-0" align="center">
    <v-col>
      <v-card variant="flat" class="pb-1">
        <v-container class="pa-0" fluid>
          <v-row class="ma-0">
            <v-col cols="auto" class="pl-0 pr-0">
              <v-icon :icon="method" size="52"></v-icon>
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
              ></v-btn>
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
</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MileageModal from '../components/MileageModal.vue'
import { useUserStore } from '@/stores/user';
import { METHODS } from 'http';


const userStore = useUserStore()
const method = ref()
const travelMethod = ref()
const loading = ref(true)
const user = ref()
const firstName = ref()

onMounted(async ()  => {
  try {
    user.value = userStore.user
    travelMethod.value = user.value.travelMethod
    firstName.value = user.value.firstName
    await getIconName(travelMethod.value)

  } catch (error){
    console.log(error)
  }
  loading.value=false
})

const getIconName= async(travelMethod) =>{
  switch (travelMethod){
    case "RUNNING":
      method.value = 'mdi-run-fast'
      break
    case "WHEELING":
      method.value = 'mdi-wheelchair-accessibility'
      break
    case "WALKING":
      method.value = 'mdi-walk'
      break
}}



const tempUserMileage = ref(100)
</script>
<style scoped></style>
