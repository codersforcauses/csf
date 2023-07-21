<template>
  <div v-if="!loading">
    <v-container>
      <v-row class="ma-0 px-13 pt-4" align="center" justify="center">
        <v-col align="center">
          <h1>Welcome back, {{ userStore.user!.username }}</h1>
        </v-col>
        <v-btn size="medium" icon="mdi-cog" variant="text" href="/settings" />
      </v-row>
      <v-divider />
      <v-row class="ma-0 px-4 pb-0 pt-0" align="center">
        <v-col>
          <v-card variant="flat" class="pb-1">
            <v-container class="pa-0" fluid>
              <v-row class="ma-0">
                <v-col cols="auto" class="pl-0 pr-0">
                  <v-icon :icon="method" size="52"></v-icon>
                </v-col>
                <v-col>
                  <v-chip color="green" class="rounded text-h5">{{ UserMileage }} KM</v-chip>
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
                  <MileageModal v-model="dialog" @handle-submit="updateChallengeProgress" />
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
      <v-divider />
      <v-row class="ma-0 pt-0 pb-0" align="center">
        <v-col>
          <h1>Daily KMs</h1>
        </v-col>
      </v-row>
      <!-- </v-container> -->

      <div class="px-2">
        <h1>Challenges</h1>
        <div v-for="challenge in challenges" :key="challenge.name" class="my-4">
          <h3>{{ challenge.name }}</h3>
          <v-row dense>
            <v-col>
              <div class="progress-bar rounded-lg">
                <div
                  :class="`rounded-lg ${challenge.colour}`"
                  :style="`width: ${calcWidth(UserMileage, challenge.length)}%`"
                ></div>
              </div>
            </v-col>
            <v-col cols="4" sm="2" lg="1">
              <div :class="`length-label rounded-lg ${challenge.colour}`">
                <h3 class="primaryWhite text-center">
                  {{ `${UserMileage}/${challenge.length}KM` }}
                </h3>
              </div>
            </v-col>
          </v-row>
        </div>
      </div>
      <v-divider />
    </v-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MileageModal from '../components/MileageModal.vue'
import { useUserStore } from '@/stores/user'
import { useMileageStore } from '@/stores/mileage'

const userStore = useUserStore()
const mileageStore = useMileageStore()

const method = ref()
const UserMileage = ref()
const loading = ref(true)
const mileageLoaded = ref(true)

const getIconName = (medium: any) => {
  switch (medium) {
    case 'RUNNING':
      method.value = 'mdi-run-fast'
      break
    case 'WHEELING':
      method.value = 'mdi-wheelchair-accessibility'
      break
    case 'WALKING':
      method.value = 'mdi-walk'
      break
  }
}

const dialog = ref(false)
const challenges = ref([
  { name: 'WOORABINDA', length: 24, colour: 'bg-secondaryGreen' },
  { name: 'WURRUMIYANGA', length: 60, colour: 'bg-secondaryBlue' },
  { name: "GALIWIN'KU", length: 84, colour: 'bg-primaryRed' },
  { name: 'PALM ISLAND', length: 120, colour: 'bg-primaryBlack' }
])

function calcWidth(travelDist: number, totalDist: number) {
  return Math.min((100 * travelDist) / totalDist, 100)
}

function updateChallengeProgress() {
  mileageStore.getMileageByUser()
  UserMileage.value = mileageStore.totalKmByUser
}

onMounted(async () => {
  if (userStore.user) {
    try {
      getIconName(userStore.user.travelMethod)
      updateChallengeProgress()
    } catch (error) {
      console.log(error)
    }
  }
  loading.value = false
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
