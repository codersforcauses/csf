<template>
  <!--Display Subteams-->
  <v-row no-gutters>
    <v-col cols="12">
      <v-row justify="space-between" no-gutters>
        <v-col cols="10">
          <v-text-field
            :rules="[state.rules.required]"
            variant="outlined"
            v-model="state.newSubTeamName"
            label="Add subteam"
          />
        </v-col>
        <v-col cols="2">
          <v-icon class="float-right" @click="addSubTeam" icon="mdi mdi-plus" size="48px" />
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="12">
      <v-list v-model:opened="state.open">
        <v-list-group value="Users">
          <template v-for="team in state.subteams" :key="team.teamName">
            <v-list-group sub-group no-action :value="team.teamName">
              <template v-slot:activator="{ props }">
                <!--avatar-->
                <v-list-item v-bind="props">
                  <v-list-item-content>
                    <!--team name-->
                    <div class="d-flex align-center">
                      {{ team.teamName }}
                      <span class="km-text rounded-lg ml-auto text-no-wrap pa-1 bg-success">
                        {{ team.totalKM }}
                      </span>

                      <v-icon
                        class="ml-5"
                        icon="mdi mdi-pencil"
                        @click="openEditSubteamDialog(team.teamId)"
                        size="16px"
                        id="pointer-cursor"
                      />
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </template>
              <v-list-item
                v-for="member in team.members"
                :key="member.firstname"
                :value="member.firstname"
                :title="member.firstname + ' ' + member.lastname"
              >
                <template v-slot:title="{ title }">
                  <v-list-item :prepend-avatar="member.avatar">
                    <v-list-item-content> {{ title }}</v-list-item-content>
                  </v-list-item>
                </template>
              </v-list-item>
            </v-list-group>
            <v-divider></v-divider>
          </template>
        </v-list-group>
      </v-list>
    </v-col>
  </v-row>
  <SubTeamsModal
    v-model="showSubTeamModal"
    @saveTeam="saveTeam"
    @removeSubTeam="removeSubTeam"
    :selectedSubteam="selectedSubteam"
    :avaliableMemeberList="state.avaliableMemeberList"
  />
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import SubTeamsModal from './SubTeamsModal.vue'

//import { type Subteam } from '../types/subteam.ts'

let selectedSubteam = reactive({
  teamName: '',
  teamId: '',
  subteamId: '',
  totalKM: '',
  members: [
    {
      id: 13,
      firstname: 'Unknown',
      lastname: 'Unknown',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    }
  ]
})

const showSubTeamModal = ref(false)
//dummy data
const state = reactive({
  newSubTeamName: '',
  open: ['Users'],
  // dialog: false,
  i: '1',
  selectedMember: null,
  rules: {
    required: (value: string) => !!value || 'Field is required'
  },
  avaliableMemeberList: [
    {
      id: 111,
      firstname: 'Ned',
      lastname: 'A',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    },
    {
      id: 131,
      firstname: 'Ned',
      lastname: 'B',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    },
    {
      id: 141,
      firstname: 'Ned',
      lastname: 'C',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    }
  ],
  subteams: [
    {
      teamName: 'Team1',
      teamId: '1',
      totalKM: '60KM',
      members: [
        {
          id: 2,
          firstname: 'Tom',
          lastname: 'A',
          avatar: 'src/assets/Avatars/avatar4.jpg'
        },
        {
          id: 3,
          firstname: 'Tom',
          lastname: 'B',
          avatar: 'src/assets/Avatars/avatar5.jpg'
        },
        {
          id: 4,
          firstname: 'Tom',
          lastname: 'C',
          avatar: 'src/assets/Avatars/avatar6.jpg'
        }
      ]
    },
    {
      teamName: 'Team2',
      teamId: '2',
      totalKM: '120KM',
      members: [
        {
          id: 11,
          firstname: 'John',
          lastname: 'A',
          avatar: 'src/assets/Avatars/avatar1.jpg'
        },
        {
          id: 12,
          firstname: 'John',
          lastname: 'B',
          avatar: 'src/assets/Avatars/avatar2.jpg'
        },
        {
          id: 13,
          firstname: 'John',
          lastname: 'C',
          avatar: 'src/assets/Avatars/avatar3.jpg'
        }
      ]
    }
  ],

  selectedSubteam: {
    teamName: '',
    teamId: '',
    totalKM: '',
    members: [
      {
        id: 13,
        firstname: 'Unknown',
        lastname: 'Unknown',
        avatar: 'https://cdn.vuetifyjs.com/images/john.png'
      }
    ]
  },
  selectedId: '',
  updatedTeamName: ''
})

const saveTeam = (selectedSubteam: any, avaliableMemeberList: any) => {
  if (selectedSubteam.teamName === '') {
    return
  }
  state.subteams = state.subteams.map((item) => {
    if (item.teamId === selectedSubteam.teamId) {
      return selectedSubteam
    }
    return item
  })
  updateAvaliableMemeberList(avaliableMemeberList)
  showSubTeamModal.value = false
}

const removeSubTeam = (teamId: string | number) => {
  // relase members to avaliableMemeberList
  const team = state.subteams.find((item) => item.teamId === teamId)
  if (team) {
    updateAvaliableMemeberList([...state.avaliableMemeberList, ...team.members])
  }
  state.subteams = state.subteams.filter((item) => item.teamId !== teamId)
  showSubTeamModal.value = false
}

const updateAvaliableMemeberList = (members: any) => {
  state.avaliableMemeberList = members
}

// team list actions
const addSubTeam = () => {
  if (state.newSubTeamName === '') {
    return
  }
  state.subteams.push({
    teamName: state.newSubTeamName,
    teamId: randomString(32),
    totalKM: '0KM',
    members: []
  })
}
const randomString = (len: number) => {
  len = len || 32
  var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
  var maxPos = $chars.length
  var pwd = ''
  for (let i = 0; i < len; i++) {
    pwd += $chars.charAt(Math.floor(Math.random() * maxPos))
  }
  return pwd
}

// ----------------- dialog actions -----------------
state.subteams.find((item) => item.teamId === state.selectedId)

const openEditSubteamDialog = (teamId: string) => {
  selectedSubteam = JSON.parse(
    JSON.stringify(state.subteams.find((item) => item.teamId === teamId))
  )
  showSubTeamModal.value = true
}
</script>

<style scoped>
.v-list-item {
  padding: 4px 10px !important;
}

.custom-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.km-text {
  color: #8c8c8c;
}

.v-input.custom-text-field input {
  font-size: 48px !important;
}
</style>
