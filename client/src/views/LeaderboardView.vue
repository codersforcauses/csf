<template>
  <div v-if="!isLoading">
    <div class="header text-white">
      <h1 class="text-center font-weight-medium text-md-h1" id="title">Leaderboards</h1>
    </div>
    <v-row class="ma-0 pt-5 pb-1" justify="space-evenly">
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
          <th id="rankColumn" class="text-right">Rank</th>
          <th id="nameColumn" class="text-left">Name</th>
          <th
            v-if="activeButton == 'Individual'"
            id="teamColumn"
            class="text-left"
            style="cursor: pointer"
            @click="sortTeam(filteredUserLeaderboard)"
          >
            Team
            <v-icon
              size="24"
              :class="{ 'mdi mdi-menu-down': !teamSorted, 'mdi mdi-menu-up': teamSorted }"
            ></v-icon>
          </th>
          <th
            id="mileageColumn"
            class="text-left"
            style="cursor: pointer"
            @click="sortMileage(filteredUserLeaderboard)"
          >
            Mileage
            <v-icon
              size="24"
              :class="{ 'mdi mdi-menu-down': !mileageSorted, 'mdi mdi-menu-up': mileageSorted }"
            ></v-icon>
          </th>
        </tr>
      </thead>
      <tbody v-if="activeButton === 'Individual'">
        <tr
          v-if="currentUser"
          style="border-collapse: separate; border-spacing: 20px"
          class="bg-grey-lighten-4"
        >
          <td v-if="currentUser.rank < 4" class="text-right text-subtitle-1">
            <v-icon icon="mdi-trophy" size="25px" :class="getTrophyColour(currentUser.rank)" />
            {{ currentUser.rank }}
          </td>
          <td v-else class="text-right text-subtitle-1">{{ currentUser.rank }}</td>
          <td class="text-subtitle-1">{{ currentUser.username }}</td>
          <td v-if="(activeButton = 'Individual')" class="text-subtitle-1">
            {{ getTeamName(currentUser.teamId) }}
          </td>
          <td>
            <v-chip color="green" class="rounded text-h6 w-100 d-flex justify-center">{{
              Math.round(currentUser.totalMileage * 100) / 100
            }}</v-chip>
          </td>
        </tr>
        <tr v-if="currentUser">
          <td id="gap"></td>
          <td id="gap"></td>
          <td id="gap"></td>
          <td id="gap"></td>
        </tr>
        <tr v-for="item in filteredUserLeaderboard" :key="item.username">
          <td v-if="item.rank < 4" class="text-right text-subtitle-1">
            <v-icon icon="mdi-trophy" size="25px" :class="getTrophyColour(item.rank)" />
            {{ item.rank }}
          </td>
          <td v-else class="text-right text-subtitle-1">{{ item.rank }}</td>
          <td class="text-subtitle-1">{{ item.username }}</td>
          <td class="text-subtitle-1">{{ getTeamName(item.teamId) }}</td>
          <td>
            <v-chip color="green" class="rounded text-h6 w-100 d-flex justify-center">{{
              Math.round(item.totalMileage * 100) / 100
            }}</v-chip>
          </td>
        </tr>
      </tbody>
      <tbody v-else>
        <tr
          v-if="currentTeam"
          style="border-collapse: separate; border-spacing: 20px"
          class="bg-grey-lighten-4"
        >
          <td v-if="currentTeam.rank < 4" class="text-right text-subtitle-1">
            <v-icon icon="mdi-trophy" size="25px" :class="getTrophyColour(currentTeam.rank)" />
            {{ currentTeam.rank }}
          </td>
          <td v-else class="text-right text-subtitle-1">{{ currentTeam.rank }}</td>
          <td class="text-subtitle-1">{{ currentTeam.name }}</td>
          <td>
            <v-chip color="green" class="rounded text-h6 w-100 d-flex justify-center">{{
              Math.round(currentTeam.totalMileage * 100) / 100
            }}</v-chip>
          </td>
        </tr>
        <tr v-if="currentTeam">
          <td id="gap"></td>
          <td id="gap"></td>
          <td id="gap"></td>
        </tr>
        <tr v-for="item in filteredTeamLeaderboard" :key="item.name">
          <td v-if="item.rank < 4" class="text-right text-subtitle-1">
            <v-icon icon="mdi-trophy" size="25px" :class="getTrophyColour(item.rank)" />
            {{ item.rank }}
          </td>
          <td v-else class="text-right text-subtitle-1">{{ item.rank }}</td>
          <td>
            <p class="text-subtitle-1">{{ item.name }}</p>
            <p class="text-body-2 text-grey">{{ shortenBio(item.bio) }}</p>
          </td>
          <td>
            <v-chip color="green" class="rounded text-h6 w-100 d-flex justify-center">{{
              Math.round(item.totalMileage * 100) / 100
            }}</v-chip>
          </td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script setup lang="ts">
import { useMileageStore } from '@/stores/mileage'
import { useUserStore } from '@/stores/user'
import { useTeamStore } from '@/stores/team'
import type {
  RankedUserLeaderboardEntry,
  RankedTeamLeaderboardEntry,
  GetLeaderboardParam,
  UserLeaderboard,
  TeamLeaderboard
} from '@/types/mileage'
import { ref, onMounted, computed } from 'vue'
import { useDisplay } from 'vuetify'
import type { Team } from '@/types/team'
const { name } = useDisplay()

const mileageStore = useMileageStore()
const userStore = useUserStore()
const teamStore = useTeamStore()
const activeButton = ref('Individual')
const searchQuery = ref('')
const userLeaderboard = ref<RankedUserLeaderboardEntry[]>([])
const teamLeaderboard = ref<RankedTeamLeaderboardEntry[]>([])
const currentUser = ref<RankedUserLeaderboardEntry | undefined>()
const currentTeam = ref<RankedTeamLeaderboardEntry | undefined>()
const teams = ref()
const isLoading = ref(true)
const teamSorted = ref(false)
const mileageSorted = ref(false)
const teamList = ref<Number[]>([])
const topTeam = ref(0)

const filteredUserLeaderboard = computed<RankedUserLeaderboardEntry[]>(() =>
  userLeaderboard.value.filter((user) =>
    user.username.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
)
const filteredTeamLeaderboard = computed<RankedTeamLeaderboardEntry[]>(() =>
  teamLeaderboard.value.filter((team) =>
    team.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
)

const maxBioLength = computed(() => {
  switch (name.value) {
    case 'xs':
      return 40
    case 'sm':
      return 80
    case 'md':
      return 160
    case 'lg':
      return 300
    default:
      return 500
  }
})

function shortenBio(bio: string) {
  if (bio.length > maxBioLength.value) {
    return bio.substring(0, maxBioLength.value) + '...'
  }
  return bio
}

function getTrophyColour(rank: number) {
  switch (rank) {
    case 1:
      return 'text-yellow-darken-1'
    case 2:
      return 'text-blue-grey-lighten-1'
    default:
      return 'text-orange-darken-1'
  }
}

onMounted(async () => {
  let userParam = { type: 'users' } as GetLeaderboardParam
  if (userStore.user) userParam.userId = userStore.user.id
  let teamParam = { type: 'teams' } as GetLeaderboardParam
  if (teamStore.team) teamParam.teamId = teamStore.team.teamId
  let usersResult = (await mileageStore.getLeaderboard(userParam)) as UserLeaderboard
  if (usersResult) {
    userLeaderboard.value = usersResult.leaderboard
    currentUser.value = usersResult.user
  }
  let teamsResult = (await mileageStore.getLeaderboard(teamParam)) as TeamLeaderboard
  if (teamsResult) {
    teamLeaderboard.value = teamsResult.leaderboard
    currentTeam.value = teamsResult.team
  }
  teams.value = (await teamStore.getTeams()) as Team[]
  await findTeams(filteredUserLeaderboard.value)
  isLoading.value = false
})

const getTeamName = (teamId: number) => {
  return teams.value.find((team: Team) => team.teamId === teamId).name
}

const findTeams = async (data: RankedUserLeaderboardEntry[]) => {
  data.forEach((element) => {
    if (!teamList.value.includes(element.teamId)) {
      teamList.value.push(element.teamId)
    }
  })
  teamList.value.sort()
}

const sortTeam = (data: RankedUserLeaderboardEntry[]) => {
  if (topTeam.value === 0) topTeam.value = 1
  if (topTeam.value === teamList.value.length + 1) {
    topTeam.value = 1
  }
  let items = <RankedUserLeaderboardEntry[]>[]
  data.forEach((element) => {
    if (element.teamId !== topTeam.value) {
      items.push(element)
    }
  })

  for (let i = 0; i < items.length; i++) {
    const index = data.indexOf(items[i])
    data.splice(index, 1)
  }
  data.push(...items)
  userLeaderboard.value = [...data]
  topTeam.value = 1 + topTeam.value
}

const sortMileage = (data: RankedUserLeaderboardEntry[]) => {
  if (!mileageSorted.value) {
    mileageSorted.value = !mileageSorted.value
    return data.sort((a, b) => a.totalMileage - b.totalMileage)
  } else {
    mileageSorted.value = !mileageSorted.value
    return data.sort((a, b) => b.totalMileage - a.totalMileage)
  }
}
</script>

<style scoped>
.header {
  background-image: url('/images/Footer-min.jpeg');
  background-size: cover;
  font-family: Hackney !important;
}

#title {
  font-family: Hackney !important;
}

#rankColumn {
  width: 80px;
}

#nameColumn {
  width: auto;
}

#teamColumn {
  width: auto;
}

#mileageColumn {
  width: 33%;
}

#gap {
  height: 10px;
}
</style>
