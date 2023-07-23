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
                      <v-icon class="ml-5" icon="mdi mdi-pencil" @click="openEditSubteamDialog(subteam.subteamId)"
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
  <SubTeamsModal v-model="showSubTeamModal" @save-subteam="saveSubteam" @delete-sub-team ="deleteSubTeam"
    :selectedSubteam="selectedSubteam!" :availableMemeberList="availableMembersList" />
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import type { SubteamView, MemberView, UserView } from '@/types/subteam'
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

let selectedSubteam = ref<SubteamView>({
  subteamId: 0,
  name: '',
  teamId: 0,
  totalKm: '0',
  members: [
    {
      id: 13,
      firstName: 'Unknown',
      lastName: 'Unknown',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    }
  ]
})
import SubTeamsModal from './SubTeamsModal.vue'
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
    // console.log(subteamViews)

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

const addSubTeam = async () => {
  if (newSubTeamName.value === '') {
    return
  }
  await subTeamStore.createSubteam({
    name: newSubTeamName.value,
    teamId: teamId.value
  });
  await subTeamStore.getSubteamsView(teamId.value)
  subteamViews.value = subTeamStore.subteamsView;
}

// ----------------- modal actions -----------------
const deleteSubTeam = async(subteamId: number) => {

  await subTeamStore.removeMembersFromSubteam(subteamId);
  await subTeamStore.deleteSubteam(subteamId);
  await subTeamStore.getAvailableMembers();
  availableMembersList.value = subTeamStore.availableMemberList;
  await subTeamStore.getSubteamsView(teamId.value);
  subteamViews.value = subTeamStore.subteamsView;

}

const saveSubteam = async(subteamId: number, newName: string,updatedSubteamMembers: MemberView[], updatedAvailableMembers: MemberView[]) => {
  if (newName !== '' && newName !== selectedSubteam.value.name) {
    await subTeamStore.updateSubteam({
      subteamId: selectedSubteam.value.subteamId,
      name: newName,
      teamId: selectedSubteam.value.teamId,
    })
  }
  // update subteam members and available members
  updateSubteamMembers(subteamId, updatedAvailableMembers, updatedSubteamMembers)
  //refresh data
  await subTeamStore.getAvailableMembers();
  availableMembersList.value = subTeamStore.availableMemberList;
  await subTeamStore.getSubteamsView(teamId.value);
  subteamViews.value = subTeamStore.subteamsView;
}

const updateSubteamMembers = async(subteamId: number, updatedAvailableMembers: MemberView[], updatedSubteamMembers: MemberView[]) => {

  const subteamMembers = subteamViews.value.find((subteam) => subteam.subteamId === subteamId)!.members;
  
  let availableMembersIdSet = new Set(availableMembersList.value.map(member => member.id));
  let updatedAvailableMembersIdSet= new Set(updatedAvailableMembers.map(member => member.id));
  let subteamMemberIdSet= new Set (subteamMembers.map(member => member.id));
  let updatedSubteamMembersIdSet = new Set(updatedSubteamMembers.map(member => member.id))
  
  updatedAvailableMembersIdSet.forEach((e) => {
    if(availableMembersIdSet.has(e)){
      updatedAvailableMembersIdSet.delete(e);
    }
  })
  updatedAvailableMembersIdSet.forEach(async(e) => {
    await subTeamStore.removeSubteamMember(e);
  });

  updatedSubteamMembersIdSet.forEach((e) => {
    if(subteamMemberIdSet.has(e)){
      updatedSubteamMembersIdSet.delete(e);
    }
  });
  updatedSubteamMembersIdSet.forEach(async(e) => {
    await subTeamStore.editUserSubteam(subteamId, e);
  });
}

// ----------------- dialog actions -----------------
const openEditSubteamDialog = async(subteamId: number) => {
  selectedSubteam.value = JSON.parse(
    JSON.stringify(subTeamStore.subteamsView.find((item) => item.subteamId === subteamId))
  )
  await subTeamStore.getAvailableMembers();
  availableMembersList.value = subTeamStore.availableMemberList;
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