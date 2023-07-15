<template>
  <v-list class="my-list" v-model:opened="data.open">
      <v-row no-gutters>
          <v-col cols="10">
              <v-text-field variant="outlined" v-model="data.newSubTeamName" label="Add subteam"></v-text-field>
          </v-col>
          <v-col cols="2">
              <v-icon @click="addSubTeam" icon="mdi mdi-plus" size="45px" class="px-6" id="pointer-cursor" />
          </v-col>
          <v-col cols="12">
              <v-list-group value="Users">
                  <template v-for="team in data.subteams" :key="team.teamName">
                      <v-list-group sub-group no-action :value="team.teamName">
                          <template v-slot:activator="{ props }">
                              <v-list-item class="abc" v-bind="props"
                                  prepend-avatar="https://cdn.vuetifyjs.com/images/john.png">
                                  <v-list-item-content>
                                      <div class="d-flex">
                                          {{ team.teamName }}
                                          <span class=" ml-auto text-no-wrap   bg-secondary">
                                              {{ team.totalKM }}
                                          </span>

                                          <v-icon class=" ml-5" icon="mdi mdi-pencil" @click="openDialog(team.teamId)"
                                              size="16px" id="pointer-cursor" />

                                      </div>
                                  </v-list-item-content>
                              </v-list-item>
                          </template>
                          <v-list-item v-for="member in team.members" :key="member.firstname" :value="member.firstname"
                              :title="member.firstname + ' ' + member.lastname">
                              <template v-slot:title="{ title }">
                                  <v-list-item prepend-avatar="https://cdn.vuetifyjs.com/images/john.png">
                                      <v-list-item-content> {{ title }}</v-list-item-content>
                                  </v-list-item>
                              </template>
                          </v-list-item>
                      </v-list-group>
                      <v-divider></v-divider>
                  </template>
              </v-list-group>
          </v-col>
      </v-row>
  </v-list>


  <v-dialog v-model="data.dialog" fullscreen transition="dialog-bottom-transition">

      <v-card>
          <v-card-text>
              <div class="text-h3">{{ data.selectedTeam?.teamName }} <v-btn variant="text" icon="mdi mdi-window-close"
                      @click="data.dialog = false"> </v-btn>
              </div>
              <div class="text-h4">{{ data.selectedTeam?.totalKM }}</div>
              <div class="text-h4">Members</div>

              <!-- allmembers -->
              <v-select :items="data.allMembers" label="Add new member" v-model="data.selectedMember" variant="underlined"
                  clearable dense @update:modelValue="addMember">
                  <template v-slot:selection="{ props, item }">
                      <v-list-item v-bind="props" :title="item.raw.firstname + ' ' + item.raw.lastname"></v-list-item>
                  </template>
                  <template v-slot:item="{ props, item }">
                      <v-list-item v-bind="props" prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
                          :title="item.raw.firstname + ' ' + item.raw.lastname"></v-list-item>
                  </template>
              </v-select>

              <!-- member list -->
              <v-list>
                  <v-list-item-group color="primary">
                      <v-list-item v-for="(member, index) in data.selectedTeam?.members" :key="index">
                          <v-list-item-content> {{ member.firstname + ' ' + member.lastname
                          }}
                              <v-icon icon="mdi mdi-window-close" size="16px" id="pointer-cursor"
                                  @click="showRemoveMemberConfirmation(member.id)" />
                          </v-list-item-content>
                      </v-list-item>
                  </v-list-item-group>
              </v-list>

          </v-card-text>
          <v-card-actions class="justify-end">
              <v-btn color="primary" variant="flat" @click="saveTeam">Save</v-btn>
              <ConfirmButton
            :action="'Save'"
            :object="'team'"
            :use-done-for-button="true"
            @handle-confirm="saveTeam"
          />
              <v-btn color="primary" variant="flat" @click="showConfirmationDialog">Delete Subteam</v-btn>
          </v-card-actions>
      </v-card>
  </v-dialog>

  <v-dialog v-model="removeMemberConfirmationDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline">Remove team member</v-card-title>
        <v-card-text>
          Are you sure you want to remove this team member?
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="cancelRemoveMemberConfirmation">
            Cancel
          </v-btn>
          <v-btn color="error" @click="confirmRemoveMember">
            Confirm
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>



  <v-dialog v-model="confirmationDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline">Confirmation</v-card-title>
        <v-card-text>Are you sure you want to delete the subteam?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="cancelDeletion">Cancel</v-btn>
          <v-btn color="error" @click="confirmDeletion">Delete</v-btn>
        </v-card-actions>
      </v-card>
  </v-dialog>

</template>

<script setup lang="ts">
import { ref, watch, reactive, toRefs, onBeforeMount, onMounted, watchEffect, computed } from 'vue';
import ConfirmButton from '@/components/ConfirmButton.vue'
defineProps(['isSubTeamsVisible'])

//dummy data
const data = reactive({
  newSubTeamName: '',
  open: ['Users'],
  dialog: false,
  i: "1",
  selectedMember: null,
  subteams: [
      {
          teamName: 'team1',
          teamId: '1',
          totalKM: "60KM",
          members: [
              {
                  id: 2,
                  firstname: "Tom",
                  lastname: "A",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
              {
                  id: 3,
                  firstname: "Tom",
                  lastname: "B",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
              {
                  id: 4,
                  firstname: "Tom",
                  lastname: "C",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
          ]
      },
      {
          teamName: 'team2',
          teamId: '2',
          totalKM: "160KM",
          members: [
              {
                  id: 11,
                  firstname: "John",
                  lastname: "A",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
              {
                  id: 12,
                  firstname: "John",
                  lastname: "B",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
              {
                  id: 13,
                  firstname: "John",
                  lastname: "C",
                  avatar: "https://cdn.vuetifyjs.com/images/john.png",
              },
          ]
      },

  ],

  allMembers: [
      {
          firstname: "Ned",
          lastname: "A",
          avatar: "https://cdn.vuetifyjs.com/images/john.png",
      },
      {
          firstname: "Ned",
          lastname: "B",
          avatar: "https://cdn.vuetifyjs.com/images/john.png",
      },
      {
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
              firstname: "Tom2133",
              lastname: "To213m3",
              avatar: "https://cdn.vuetifyjs.com/images/john.png",
          },
      ]
  },
  selectedId: '',

})

data.subteams.find((item) => item.teamId === data.selectedId)

const openDialog = (teamId) => {
  data.dialog = true
  data.selectedTeam = ref(Object.assign({}, data.subteams.find((item) => item.teamId === teamId)))
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
  const randomString=(len) =>{
   len = len || 32;
   var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
  var maxPos = $chars.length;
   var pwd = '';
   for (let i = 0; i < len; i++) {
   pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
 }
  return pwd;
 }
const removeMember = (memberId) => {
  console.log(memberId);
  //    update selectedteam
  data.selectedTeam.members = data.selectedTeam.members.filter((item) => item.id !== memberId)
}
const addMember = () => {

  if (data.selectedMember) {
      //    update selectedteam
      data.selectedTeam.members.push(data.selectedMember)
      //    update allmembers
      data.selectedMember = null
  }
}
const saveTeam = () => {
  // copy selectedteam to subteams
  alert('save')
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

const confirmationDialog = ref(false);
const showConfirmationDialog = () => {
  confirmationDialog.value = true;
};

const cancelDeletion = () => {
  confirmationDialog.value = false;
};

const confirmDeletion = () => {
  removeSubTeam();
  confirmationDialog.value = false;
};

const removeMemberConfirmationDialog = ref(false);

const showRemoveMemberConfirmation = (memberId) => {
 removeMemberConfirmationDialog.value = memberId;
 console.log(memberId)
}
const cancelRemoveMemberConfirmation = () => {
  removeMemberConfirmationDialog.value = false;
}
const confirmRemoveMember = () => {
  removeMember(removeMemberConfirmationDialog.value);
  cancelRemoveMemberConfirmation();
}


</script>
<style scoped  >
.v-list-item {
  padding: 4px 10px !important;
}

.my-list {
  width: 100%;
  max-width: 700px;

}
</style>

<!-- export interface User {
id: Number
username: string
firstName: string
lastName: string
email: string
avatar: string
travelMethod: string
teamSignup: boolean
hasConsent: boolean
subteamId?: number
teamId?: number
teamAdmin?: Boolean
} -->