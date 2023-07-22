<template>
  <!--Display Subteams-->
  <v-row no-gutters>
    <v-col cols="12">
      <v-row justify="space-between" no-gutters>
        <v-col cols="10">
          <v-text-field :rules="[rules.required]" variant="outlined" v-model="newSubTeamName" label="Add subteam" />
        </v-col>
        <v-col cols="2">
          <v-icon class="float-right" @click="addSubTeam" icon="mdi mdi-plus" size="48px" />
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="12">
      <v-list v-model:opened="state.open">
        <v-list-group value="Users">
          <template v-for="subteam in subteamViews" :key="subteam.name">
            <v-list-group sub-group no-action :value="subteam.subteamId">
              <template v-slot:activator="{ props }">
                <v-list-item v-bind="props">
                  <v-list-item-content>
                    <!--Subteam Info-->
                    <div class="d-flex align-center">
                      {{ subteam.name }}
                      <span class="km-text rounded-lg ml-auto text-no-wrap pa-1 bg-success">
                        {{ subteam.totalKm }}
                      </span>
                      <!--Edit Subteam Pencil Icon-->
                      <v-icon class="ml-5" icon="mdi mdi-pencil" @click="openEditSubteamDialog(subteam.teamId)"
                        size="16px" id="pointer-cursor" />
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </template>
              <!--Member List-->
              <v-list-item v-for="member in subteam.members" :key="member.id" :value="member.firstName"
                :title="member.firstName + ' ' + member.lastName">               
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
  <SubTeamsModal v-model="showSubTeamModal" @saveTeam="saveTeam" @removeSubTeam="removeSubTeam"
    :selectedSubteam="selectedSubteam" :availableMemeberList="availableMembersList" />
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import SubTeamsModal from './SubTeamsModal.vue'
import type { SubteamView, UserView } from '@/types/subteam'
import { useSubTeamStore } from '@/stores/subTeam'
import { onMounted } from 'vue';
import { notify } from '@kyvg/vue3-notification'
import { useUserStore } from '@/stores/user'

const state=reactive({
  open: ['Users']
})

const rules = ref({
  required: (value: string) => !!value || 'Field is required'
})

let selectedSubteam = ref({
  name: '',
  teamId: 0,
  subteamId: 0,
  totalKm: '',
  members: [
    {
      id: 13,
      firstName: 'Unknown',
      lastName: 'Unknown',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    }
  ]
})

const showSubTeamModal = ref(false)

const userStore = useUserStore();
const subTeamStore = useSubTeamStore();

const teamId = ref(-1)

if (userStore.user && userStore.user.teamId) {
  teamId.value = userStore.user.teamId;
}

const availableMembersList = ref<UserView[]>([])
let subteamViews = ref<SubteamView[]>([])

//Loading data
onMounted(async () => {
  try {
    await subTeamStore.getAvailableMembers();
    availableMembersList.value = subTeamStore.availableMemberList;

    await subTeamStore.getSubteamsView(teamId.value);
    subteamViews.value = subTeamStore.subteamsView;

  } catch (e) {
    console.log(e)
    notify({
      title: 'Get Subteams',
      type: 'error',
      text: 'Loading error'
    })
  }
});

// create new subteam
const newSubTeamName = ref('')
const addSubTeam = () => {
  if (newSubTeamName.value === '') {
    return
  }
  subTeamStore.createSubteam({
    name: newSubTeamName.value,
    teamId: teamId.value
  });
  subTeamStore.getSubteamsView(teamId.value)
  subteamViews.value = subTeamStore.subteamsView;
}

//TODO
// ----------------- modal actions -----------------
const saveTeam = (selectedSubteam: any, avaliableMemeberList: any) => {
  if (selectedSubteam.teamName === '') {
    return
  }
  subteamViews.value = subteamViews.value.map((item) => {
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
  const team = subteamViews.value.find((item) => item.teamId === teamId)
  if (team) {
    updateAvaliableMemeberList([...availableMembersList.value, ...team.members])
  }
  subteamViews.value = subteamViews.value.filter((item) => item.teamId !== teamId)
  showSubTeamModal.value = false
}

const updateAvaliableMemeberList = (members: any) => {
  availableMembersList.value = members
}

// ----------------- dialog actions -----------------
const openEditSubteamDialog = (teamId: number) => {
  selectedSubteam.value = JSON.parse(
    JSON.stringify(subteamViews.value.find((item) => item.teamId === teamId))
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