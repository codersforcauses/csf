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
      <h1>Daily KMs</h1>
    </v-col>
  </v-row>
  <v-divider />
  <div class="px-4">
    <h1>Challenges</h1>
    <div v-for="challenge in challenges" class="my-4">
      <h3>{{ challenge.name }}</h3>
      <v-row dense>
        <v-col>
          <div class="progress-bar rounded-lg">
            <div
              :class="`rounded-lg ${challenge.colour}`"
              :style="`width: ${calcWidth(distanceTravelled, challenge.length)}%`"
            ></div>
          </div>
        </v-col>
        <v-col cols="3" sm="2" lg="1">
          <div :class="`length-label rounded-lg ${challenge.colour}`">
            <h3 class="primaryWhite text-center">{{ challenge.length + 'KM' }}</h3>
          </div>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MileageModal from '../components/MileageModal.vue'
import { useUserStore } from '@/stores/user'
import server from '@/utils/server'
import { onMounted } from 'vue'
import camelize from 'camelize-ts'
import type { Mileage } from '@/types/mileage'

const userStore = useUserStore()

const tempUserFirstName = ref('John')
const tempUserMileage = ref(100)
const dialog = ref(false)
const challenges = ref([
  { name: 'WOORABINDA', length: 24, colour: 'bg-secondaryGreen' },
  { name: 'WURRUMIYANGA', length: 60, colour: 'bg-secondaryBlue' },
  { name: "GALIWIN'KU", length: 84, colour: 'bg-primaryRed' },
  { name: 'PALM ISLAND', length: 120, colour: 'bg-primaryBlack' }
])
const distanceTravelled = ref(0)

function calcWidth(travelDist: number, totalDist: number) {
  return Math.min((100 * travelDist) / totalDist, 100)
}

async function getRecentMileage() {
  if (userStore.authUser) {
    let userId = userStore.user.id
    return await server
      .get(`mileage/get_mileage/${userId}`, {
        params: {
          challenge: true
        }
      })
      .then((res) => {
        if (res.status == 200) {
          let recentMileage = camelize(res.data) as Mileage[]
          return recentMileage.reduce((a, b) => a + b.kilometres, 0)
        }
        return 0
      })
  }
  return 0
}
onMounted(async () => {
  distanceTravelled.value = await getRecentMileage()
})
</script>

<style scoped>
.progress-bar {
  background-color: #e2e2e2;
}

.progress-bar > div,
.length-label {
  height: 30px;
}
</style>
