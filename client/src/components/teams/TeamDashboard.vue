<template>
  <v-container>
    <v-row class="mx-6" :fullscreen="mobile">
      <!-- Team Name -->
      <v-row align="center" class="my-2 px-5">
        <v-col align="center">
          <h1>{{ teamData.team_name }}</h1>
        </v-col>
        <EditTeamInfo />
      </v-row>
      <v-divider />

      <!-- Total Kilometres -->
      <v-row align="center" class="my-2">
        <v-icon :class="['mdi','ml-3', getIconName(userStore.user!.travelMethod)]" size="50px" />
        <v-col>
          <v-chip color="green" class="rounded text-h5">{{ totalKilometres }} KM</v-chip>
          <h3>TOTAL</h3>
        </v-col>
      </v-row>
      <v-divider />

      <!-- Invite Code -->
      <v-row align="center" class="my-2">
        <v-col>
          <h2>Invite Code</h2>
          <p class="invite-code">{{ teamData.invite_code }}</p>
        </v-col>
        <v-tooltip location="end">
          <template v-slot:activator="{ props }">
            <v-icon
              @click="copyInviteCode"
              v-bind="props"
              class="mdi mdi-clipboard-multiple-outline px-10"
              size="32px"
            />
          </template>
          <span>{{ copyHoverText }}</span>
        </v-tooltip>
      </v-row>
      <v-divider />

      <!-- Bio -->
      <v-row id="pointer-cursor" class="my-2">
        <v-col @click="isBioVisible = !isBioVisible">
          <h2>Bio</h2>
          <p v-if="isBioVisible">{{ teamData.bio }}</p>
        </v-col>
        <v-icon
          v-if="isBioVisible"
          icon="mdi mdi-chevron-down"
          @click="isBioVisible = !isBioVisible"
          class="px-10"
          size="50px"
        />
        <v-icon
          v-else
          icon="mdi mdi-chevron-right"
          @click="isBioVisible = !isBioVisible"
          class="px-10"
          size="50px"
        />
      </v-row>
      <v-divider></v-divider>

      <!-- Daily Kilometres -->
      <v-row align="start" id="pointer-cursor" class="my-2">
        <v-col>
          <h2>Daily KMs</h2>
          <MileageGraph v-if="isDailyKmsVisible" :teamPage="true"/>
        </v-col>
        <v-icon
          v-if="isDailyKmsVisible"
          @click="isDailyKmsVisible = !isDailyKmsVisible"
          icon="mdi mdi-chevron-down"
          size="50px"
          class="px-10"
        />
        <v-icon
          v-else
          @click="isDailyKmsVisible = !isDailyKmsVisible"
          icon="mdi mdi-chevron-right"
          size="50px"
          class="px-10"
        />
      </v-row>
      <v-divider />

      <!-- Sub-teams -->
      <v-row align="start" class="my-2">
        <v-col id="pointer-cursor" @click="isSubTeamsVisible = !isSubTeamsVisible">
          <h2>Sub-Teams</h2>
          <!-- <p v-if="isSubTeamsVisible">Leave this for now</p> -->
        </v-col>
        <!-- <v-icon icon="mdi mdi-plus" size="45px" class="px-6" id="pointer-cursor" /> -->
        <v-icon
          v-if="isSubTeamsVisible"
          icon="mdi mdi-chevron-down"
          @click="isSubTeamsVisible = !isSubTeamsVisible"
          size="50px"
          id="pointer-cursor"
          class="px-10"
        />
        <v-icon
          v-else
          icon="mdi mdi-chevron-right"
          @click="isSubTeamsVisible = !isSubTeamsVisible"
          size="50px"
          id="pointer-cursor"
          class="px-10"
        />
      </v-row>
      <v-col cols="12" class="w-100" id="pointer-cursor">
        <SubTeams v-if="isSubTeamsVisible" />
      </v-col>
      <v-divider />

      <!-- Leaderboard -->
      <v-row
        align="start"
        @click="isLeaderboardVisible = !isLeaderboardVisible"
        id="pointer-cursor"
        class="my-2"
      >
        <v-col>
          <h2>Leaderboard</h2>
          <p v-if="isLeaderboardVisible">Leave this for now</p>
        </v-col>
        <v-icon v-if="isLeaderboardVisible" icon="mdi mdi-chevron-down" size="50px" class="px-10" />
        <v-icon v-else icon="mdi mdi-chevron-right" size="50px" class="px-10" />
      </v-row>
      <v-divider class="mb-10" />
    </v-row>
  </v-container>

  <!-- Leave/Delete Team -->
  <v-row justify="center" class="ma-5">
    <v-btn
      size="large"
      color="red white--text"
      v-if="userStore.user!.teamAdmin"
      @click="deleteTeam"
    >
      Delete Team
    </v-btn>
    <v-btn size="large" color="red white--text" v-else @click="removeTeam">Leave Team</v-btn>
  </v-row>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useDisplay } from 'vuetify'
import EditTeamInfo from './EditTeamInfo.vue'
import SubTeams from './SubTeams.vue'
import MileageGraph from '../MileageGraph.vue'
const { mobile } = useDisplay()
import { useTeamStore } from '@/stores/team'
import { useUserStore } from '@/stores/user'
import { useMileageStore } from '@/stores/mileage'

const teamStore = useTeamStore()
const userStore = useUserStore()
const mileageStore = useMileageStore()

onMounted(async () => {
  if (userStore.user!.teamId) await teamStore.getTeam(userStore.user!.teamId)
  updateTeamMileage()
})
const deleteTeam = () => {
  teamStore.deleteTeam()
}
const removeTeam = () => {
  teamStore.removeTeam()
}

const updateTeamMileage = () =>{
  mileageStore.getMileageByTeam()
  totalKilometres.value = mileageStore.totalKmByTeam
}

const totalKilometres = ref()

const teamData = ref({
  team_name: teamStore.team ? teamStore.team.name : '',
  total_kilometres: 0,
  invite_code: teamStore.team ? teamStore.team.joinCode : '',
  bio: teamStore.team ? teamStore.team.bio : '',
  daily_kms: [],
  sub_teams: [],
  leaderboard: []
})

watch(teamStore.team!, (newTeam) => {
  // Update the teamData when the team value changes
  if (newTeam) {
    teamData.value.team_name = newTeam.name
    teamData.value.bio = newTeam.bio
    teamData.value.invite_code = newTeam.joinCode
  }
})

const isBioVisible = ref(false)
const isDailyKmsVisible = ref(true)
const isSubTeamsVisible = ref(false)
const isLeaderboardVisible = ref(false)

const copyHoverText = ref('Copy to Clipboard')

const copyInviteCode = () => {
  navigator.clipboard.writeText(teamData.value.invite_code)
  copyHoverText.value = 'Copied!'

  setTimeout(() => {
    copyHoverText.value = 'Copy Invite Code'
  }, 2000)
}

const getIconName = (medium: string) => {
  switch (medium) {
    case 'RUNNING':
      return 'mdi-run-fast'
    case 'WHEELING':
      return 'mdi-wheelchair-accessibility'
    case 'WALKING':
      return 'mdi-walk'
  }
}
</script>

<style scoped>
h1,
h2,
.v-icon {
  color: black;
}

.totalKms {
  font-size: 1.5rem;
}

.mdi-clipboard-multiple-outline:active {
  translate: 0px 2px;
}

#pointer-cursor {
  cursor: pointer;
}

.invite-code {
  font-size: 0.7rem;
}
</style>
