<template>
  <!--Display Subteams-->
  <v-row no-gutters>
    <v-col cols="12">
      <v-row justify="space-between" no-gutters>
        <v-col cols="10">
          <v-text-field :rules="[data.rules.required]" variant="outlined" v-model="data.newSubTeamName"
            label="Add subteam" />
        </v-col>
        <v-col cols="2">
          <v-icon class="float-right" @click="addSubTeam" icon="mdi mdi-plus" size="48px" />
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="12">
      <v-list   v-model:opened="data.open">

        <v-list-group  value="Users">
          <template v-for="team in data.subteams" :key="team.teamName">
            <v-list-group sub-group no-action :value="team.teamName">
              <template v-slot:activator="{ props }">
                <!--avatar-->
                <v-list-item v-bind="props">
                  <v-list-item-content>
                    <!--team name-->
                    <div class="d-flex align-center">
                      {{ team.teamName }}
                      <span class=" km-text rounded-lg ml-auto text-no-wrap pa-1 bg-success ">
                        {{ team.totalKM }}
                      </span>

                      <v-icon class=" ml-5" icon="mdi mdi-pencil" @click="openEditSubteamDialog(team.teamId)" size="16px"
                        id="pointer-cursor" />

                    </div>
                  </v-list-item-content>
                </v-list-item>
              </template>
              <v-list-item v-for="member in team.members" :key="member.firstname" :value="member.firstname"
                :title="member.firstname + ' ' + member.lastname">
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

  <!--Edit Subteam-->
  <v-dialog v-model="data.dialog" fullscreen transition="dialog-bottom-transition">
    <v-img src="/images/Footer-min.jpeg" width="100%" max-height="32" cover />
    <v-card>
      <v-card-text>
        <!--Subteam Name-->
        <v-btn class="ma-0 pa-0 float-right " variant="text" icon="mdi mdi-window-close" @click="data.dialog = false" />
        <div class="font-weight-bold  my-6  text-h4">Edit Subteam</div>
        <div class=" w-100 d-flex flex-column text-center align-center justify-center">
          <v-text-field variant="solo" v-model="data.selectedTeam.teamName" :rules="[data.rules.required]"
            label="Edit subteam name" required dense class="text-h3 w-75 py-3 custom-text-field" />
        </div>
        <v-divider class="my-4" color="info"></v-divider>



        <!--Members-->
        <div class="font-weight-bold my-6  text-h4">Members</div>
        
        <!--Add New Member-->
        <v-select :items="data.allMembers" label="Select member" v-model="data.selectedMember" dense
          @update:modelValue="addMember">
          <template v-slot:selection="{ props, item }">
            <v-list-item v-bind="props" :title="item.raw.firstname + ' ' + item.raw.lastname"></v-list-item>
          </template>
          <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props" prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
              :title="item.raw.firstname + ' ' + item.raw.lastname" />
            <v-divider color="info"></v-divider>
          </template>
        </v-select>

        <!--Member List-->
        <v-list>
          <v-list-item v-for="(member, index) in data.selectedTeam?.members" :key="index">
            <v-list-item-content>
              <v-avatar>
                <img :src= member.avatar alt="Avatar" class="custom-avatar">
              </v-avatar>
              <span class="ml-3 font-weight-bold">
                {{
                  member.firstname + ' ' + member.lastname
                }}
              </span>
              <!--remove member icon-->
              <v-icon
                  class="float-right"
                  icon="mdi mdi-window-close"
                  size="24px"
                  id="pointer-cursor"
                  @click="display = true"
                />
                <PopupDialog
                  v-model="display"
                  :title="'Remove Team Member'"
                  :text="`Are you sure you wish to remove this member?`"
                  :submit-text="'Confirm'"
                  @handle-submit="removeMember(member.id)"
                />
            </v-list-item-content>
            <v-divider class="mt-4" color="info"></v-divider>
          </v-list-item>
        </v-list>
        <!--Buttons-->       
        <div class="w-100 d-flex justify-center">
          <v-btn color="success" class="mr-8" variant="flat" @click="saveTeam">Save</v-btn>
          <ConfirmButton
            :action="'delete'"
            :object="'subteam'"
            :use-done-for-button="false"
            @handle-confirm="removeSubTeam"
          /> 
        </div> 
      </v-card-text>
    </v-card>
</v-dialog>

</template>

<script setup lang="ts">
import { ref, reactive, toRefs} from 'vue';

import ConfirmButton from '@/components/ConfirmButton.vue'
import PopupDialog from '@/components/PopupDialog.vue'

//import { type Subteam } from '../types/subteam.ts'

defineProps(['isSubTeamsVisible'])

//dummy data
const data = reactive({
  newSubTeamName: '',
  open: ['Users'],
  dialog: false,
  i: "1",
  selectedMember: null,
  rules: {
    required: (value: string) => !!value || 'Field is required',
  },
  subteams: [
      {
          teamName: 'Team1',
          teamId: '1',
          totalKM: "60KM",
          members: [
              {
                  id: 2,
                  firstname: "Tom",
                  lastname: "A",
                  avatar: "src/assets/Avatars/avatar4.jpg",
              },
              {
                  id: 3,
                  firstname: "Tom",
                  lastname: "B",
                  avatar: "src/assets/Avatars/avatar5.jpg",
              },
              {
                  id: 4,
                  firstname: "Tom",
                  lastname: "C",
                  avatar: "src/assets/Avatars/avatar6.jpg",
              },
          ]
      },
      {
          teamName: 'Team2',
          teamId: '2',
          totalKM: "120KM",
          members: [
              {
                  id: 11,
                  firstname: "John",
                  lastname: "A",
                  avatar: "src/assets/Avatars/avatar1.jpg",
              },
              {
                  id: 12,
                  firstname: "John",
                  lastname: "B",
                  avatar: "src/assets/Avatars/avatar2.jpg",
              },
              {
                  id: 13,
                  firstname: "John",
                  lastname: "C",
                  avatar: "src/assets/Avatars/avatar3.jpg",
              },
          ]
      },

  ],

  allMembers: [
      {
          id: '111',
          firstname: "Ned",
          lastname: "A",
          avatar: "https://cdn.vuetifyjs.com/images/john.png",
      },
      {
          id: '131',
          firstname: "Ned",
          lastname: "B",
          avatar: "https://cdn.vuetifyjs.com/images/john.png",
      },
      {
          id: '141',
          firstname: "Ned",
          lastname: "C",
          avatar: "https://cdn.vuetifyjs.com/images/john.png",
      },
  ],
  selectedTeam: {
      teamName: '',
      teamId: '',
      totalKM: '',
      members: [
          {
              id: 13,
              firstname: "Tom",
              lastname: "T",
              avatar: "https://cdn.vuetifyjs.com/images/john.png",
          },
      ]
  },
  selectedId: '',
  updatedTeamName: '',
})

data.subteams.find((item) => item.teamId === data.selectedId)

const openEditSubteamDialog = (teamId: string) => {
  data.dialog = true
  data.selectedMember = null
  data.selectedTeam = reactive(JSON.parse(JSON.stringify(data.subteams.find((item) => item.teamId === teamId))))
  data.selectedId = teamId
}

const addSubTeam = () => {
  if(data.newSubTeamName === ''){return} 
  data.subteams.push({
      teamName: data.newSubTeamName,
      teamId: randomString(32),
      totalKM: "0KM",
      members: []
})

}
  const randomString=(len:number) =>{
    len = len || 32;
    var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
    var maxPos = $chars.length;
    var pwd = '';
    for (let i = 0; i < len; i++) {
      pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
    }
      return pwd;
 }
const removeMember = (memberId:string|number) => {
  data.selectedTeam.members = data.selectedTeam.members.filter((item) => item.id !== memberId)
}
const addMember = () => {

  if (data.selectedMember) {
    data.selectedTeam.members.push(data.selectedMember)
  }
}
const saveTeam = () => {
  if (data.selectedTeam.teamName === '') {
    return
  } 
  data.subteams = data.subteams.map((item) => {
      if (item.teamId === data.selectedId) {
          return data.selectedTeam
      }
      return item
  })
  data.dialog = false
}

const removeSubTeam = () => {
  data.subteams = data.subteams.filter((item) => item.teamId !== data.selectedId)
  data.dialog = false
}

defineExpose({
  ...toRefs(data)
})

const display = ref(false)
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