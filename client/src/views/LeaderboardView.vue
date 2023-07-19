<template>
  <div class="header">
    <h1 class="text-center text-secondaryTint font-weight-medium text-md-h1" id="title">
      Leaderboards
    </h1>
  </div>
  <v-row class="ma-0 pt-4" justify="space-evenly">
    <v-btn
      variant="flat"
      density="compact"
      width="120px"
      :color="activeButton === board ? 'rgb(52, 94, 158, 0.3)' : ''"
      :class="activeButton === board ? 'text-secondaryBlue' : 'black'"
      v-for="board in ['Individual', 'Teams']"
      :key="board"
      rounded="xl"
      @click="activeButton = board"
      >{{ board }}</v-btn
    >
  </v-row>
  <v-row class="ma-0 pa-4">
    <v-text-field
      prepend-inner-icon="mdi-magnify"
      hide-details
      variant="outlined"
      placeholder="Search Leaderboard"
      class="mx-3"
      clearable
      v-model="searchQuery"
    />
  </v-row>

  <v-table fixed-header class="mx-8">
    <thead>
      <tr>
        <th class="text-right w-0">Rank</th>
        <th class="text-left">Name</th>
        <th class="text-left">Mileage</th>
      </tr>
    </thead>
    <tbody v-if="activeButton === 'Individual'">
      <tr v-if="currentUser" style="border-collapse: separate; border-spacing: 20px;">
        <td v-if="currentUser.rank < 4" class="text-right w-0">
          <v-icon icon="mdi-trophy" size="20px" :class="getTrophyColour(currentUser.rank)" /> {{ currentUser.rank }}
        </td>
        <td v-else class="text-right w-0">{{ currentUser.rank }}</td>
        <td>{{ currentUser.username }}</td>
        <td>{{ currentUser.totalMileage }}</td>
      </tr>
      <!-- What follows is a dumb way of making a gap in the table -->
      <tr v-if="currentUser"><td></td><td></td><td></td></tr> 
      <tr v-for="item in filteredUserLeaderboard" :key="item.username">
        <td v-if="item.rank < 4" class="text-right w-0">
          <v-icon icon="mdi-trophy" size="20px" :class="getTrophyColour(item.rank)" /> {{ item.rank }}
        </td>
        <td v-else class="text-right w-0">{{ item.rank }}</td>
        <td>{{ item.username }}</td>
        <td>{{ item.totalMileage }}</td>
      </tr>
    </tbody>
    <tbody v-else>
      <tr v-if="currentTeam" style="border-collapse: separate; border-spacing: 20px;">
        <td v-if="currentTeam.rank < 4" class="text-right w-0">
          <v-icon icon="mdi-trophy" size="20px" :class="getTrophyColour(currentTeam.rank)" /> {{ currentTeam.rank }}
        </td>
        <td v-else class="text-right w-0">{{ currentTeam.rank }}</td>
        <td>{{ currentTeam.name }}</td>
        <td>{{ currentTeam.totalMileage }}</td>
      </tr>
      <!-- What follows is a dumb way of making a gap in the table -->
      <tr v-if="currentTeam"><td></td><td></td><td></td></tr> 
      <tr v-for="item in filteredTeamLeaderboard" :key="item.name">
        <td v-if="item.rank < 4" class="text-right w-0">
          <v-icon icon="mdi-trophy" size="20px" :class="getTrophyColour(item.rank)" /> {{ item.rank }}
        </td>
        <td v-else class="text-right w-0">{{ item.rank }}</td>
        <td>{{ item.name }}</td>
        <!--  use bio too -->
        <td>{{ item.totalMileage }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup lang="ts">
import { useMileageStore } from '@/stores/mileage'
import { useUserStore } from '@/stores/user'
import { useTeamStore } from '@/stores/team'
import type {
  UserLeaderboardEntry,
  RankedUserLeaderboardEntry,
  TeamLeaderboardEntry,
  RankedTeamLeaderboardEntry,
  GetLeaderboardParam,
  UserLeaderboard,
  TeamLeaderboard
} from '@/types/mileage'
import { ref, onMounted, computed } from 'vue'

const mileageStore = useMileageStore()
const userStore = useUserStore()
const teamStore = useTeamStore()
const activeButton = ref('Individual')
const searchQuery = ref('')
const userLeaderboard = ref<RankedUserLeaderboardEntry[]>([])
const teamLeaderboard = ref<RankedTeamLeaderboardEntry[]>([])
const currentUser = ref<RankedUserLeaderboardEntry | undefined>()
const currentTeam = ref<RankedTeamLeaderboardEntry | undefined>()

const filteredUserLeaderboard = computed<RankedUserLeaderboardEntry[]>(() =>
  userLeaderboard.value.filter((user) => user.username.toLowerCase().includes(searchQuery.value))
)
const filteredTeamLeaderboard = computed<RankedTeamLeaderboardEntry[]>(() =>
  teamLeaderboard.value.filter((team) => team.name.toLowerCase().includes(searchQuery.value))
)

function getTrophyColour(rank: number) {
  switch (rank) {
    case 1:
      return "text-yellow-darken-1"
    case 2:
      return "text-blue-grey-lighten-1"
    default:
      return "text-orange-darken-1"
  }
}

onMounted(async () => {
  let userParam = {type:'users'} as GetLeaderboardParam
  if (userStore.user) userParam.username = userStore.user.username
  let teamParam = {type:'teams'} as GetLeaderboardParam
  if (teamStore.team) teamParam.teamName = teamStore.team.name
  let usersResult = await mileageStore.getLeaderboard(userParam)
  if (usersResult) {
    usersResult = usersResult as UserLeaderboard
    let users = usersResult.leaderboard as UserLeaderboardEntry[]
    let users2: RankedUserLeaderboardEntry[] = []
    users.forEach((user, index) => {
      if (index > 0 && user.totalMileage === users[index - 1].totalMileage) {
        users2.push({ ...user, rank: users2[index - 1].rank })
      } else {
        users2.push({ ...user, rank: index + 1 })
      }
    })
    userLeaderboard.value = users2
    currentUser.value = usersResult.user
  }
  let teamsResult = await mileageStore.getLeaderboard(teamParam)
  if (teamsResult) {
    teamsResult = teamsResult as TeamLeaderboard
    let teams = teamsResult.leaderboard as TeamLeaderboardEntry[]
    let teams2: RankedTeamLeaderboardEntry[] = []
    teams.forEach((team, index) => {
      if (index > 0 && team.totalMileage === teams[index - 1].totalMileage) {
        teams2.push({ ...team, rank: teams2[index - 1].rank })
      } else {
        teams2.push({ ...team, rank: index + 1 })
      }
    })
    teamLeaderboard.value = teams2
    currentTeam.value = teamsResult.team
    }

})
</script>

<style>
.header {
  background-image: url('/images/Footer-min.jpeg');
  background-size: cover;
  font-family: Hackney !important;
}

#title {
  font-family: Hackney !important;
}
</style>
