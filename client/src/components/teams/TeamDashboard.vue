<template>
  <v-container>
    <v-row class="mx-6" :fullscreen="mobile">
      <!-- Team Name -->
      <v-row class="my-2">
        <v-col align="center">
          <h1>{{ teamData.team_name }}</h1>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Total Kilometres -->
      <v-row align="center" class="my-2">
        <v-icon class="mdi mdi-run-fast ml-3" size="50px"></v-icon>
        <v-col>
          <h2 class="totalKms">{{ teamData.total_kilometres }} KM</h2>
          <h3>TOTAL</h3>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Invite Code -->
      <v-row align="center" class="my-2">
        <v-col>
          <h2>Invite Code</h2>
          <p class="invite-code">{{ teamData.invite_code }}</p>
        </v-col>
        <v-col align="end" class="px-5">
          <v-icon
            @click="copyInviteCode"
            class="mdi mdi-clipboard-multiple-outline"
            size="32px"
          ></v-icon>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Bio -->
      <v-row id="pointer-cursor" class="my-2">
        <v-col @click="toggleBio">
          <h2>Bio</h2>
          <p v-show="isBioVisible">{{ teamData.bio }}</p>
        </v-col>
        <v-col align="end" class="px-3">
          <v-icon
            v-if="user.is_admin"
            icon="mdi mdi-pencil"
            size="32px"
            @click="editBioDialog = true"
            class="px-6"
          ></v-icon>
          <v-dialog v-model="editBioDialog" width="auto">
            <v-card>
              <v-card-text>
                What would you like to set the {{ teamData.team_name }} bio to?
              </v-card-text>
              <v-textarea v-model="newBioText" placeholder="Bio"></v-textarea>
              <v-card-actions>
                <v-btn @click="editBio">Submit</v-btn>
                <v-btn @click="editBioDialog = false">Cancel</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-icon
            v-show="isBioVisible"
            icon="mdi mdi-chevron-down"
            @click="toggleBio"
            size="50px"
          ></v-icon>
          <v-icon
            v-show="!isBioVisible"
            icon="mdi mdi-chevron-right"
            @click="toggleBio"
            size="50px"
          ></v-icon>
          <!-- if admin, click to edit bio -->
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Daily Kilometres -->
      <v-row align="start" @click="toggleDailyKms" id="pointer-cursor" class="my-2">
        <v-col>
          <h2>Daily KMs</h2>
          <p v-show="isDailyKmsVisible">daily Km's chart goes here</p>
        </v-col>
        <v-col align="end" class="px-3">
          <v-icon v-show="isDailyKmsVisible" icon="mdi mdi-chevron-down" size="50px"></v-icon>
          <v-icon v-show="!isDailyKmsVisible" icon="mdi mdi-chevron-right" size="50px"></v-icon>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Sub-teams -->
      <v-row align="start" class="my-2">
        <v-col id="pointer-cursor" @click="toggleSubTeams">
          <h2>Sub-Teams</h2>
          <p v-show="isSubTeamsVisible">Leave this for now</p>
        </v-col>
        <v-col align="end" class="px-3">
          <v-icon icon="mdi mdi-plus" size="45px" class="px-6" id="pointer-cursor"></v-icon>
          <v-icon
            v-show="isSubTeamsVisible"
            icon="mdi mdi-chevron-down"
            @click="toggleSubTeams"
            size="50px"
            id="pointer-cursor"
          ></v-icon>
          <v-icon
            v-show="!isSubTeamsVisible"
            icon="mdi mdi-chevron-right"
            @click="toggleSubTeams"
            size="50px"
            id="pointer-cursor"
          ></v-icon>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <!-- Leaderboard -->
      <v-row align="start" @click="toggleLeaderboard" id="pointer-cursor" class="my-2">
        <v-col>
          <h2>Leaderboard</h2>
          <p v-show="isLeaderboardVisible">Leave this for now</p>
        </v-col>
        <v-col align="end" class="px-3">
          <v-icon v-show="isLeaderboardVisible" icon="mdi mdi-chevron-down" size="50px"></v-icon>
          <v-icon v-show="!isLeaderboardVisible" icon="mdi mdi-chevron-right" size="50px"></v-icon>
        </v-col>
      </v-row>
      <v-divider class="mb-10"></v-divider>
    </v-row>
  </v-container>

  <!-- Leave/Delete Team -->
  <v-row class="ma-5" justify="center">
    <v-btn size="large" color="red white--text" v-if="user.is_admin">
      Remove Team Member
      <v-dialog v-model="removeDialog" activator="parent" width="auto">
        <v-card>
          <v-card-text> Add functionality for deleting team members </v-card-text>
          <v-card-actions>
            <v-btn @click="deleteTeamMember">Delete Team Member</v-btn>
            <v-btn @click="removeDialog = false">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-btn>
  </v-row>
  <v-row justify="center">
    <v-btn size="large" color="red white--text" v-if="user.is_admin">
      Delete Team
      <v-dialog v-model="deleteDialog" activator="parent" width="auto">
        <v-card>
          <v-card-text>
            Are you sure you want to completely delete the team {{ teamData.team_name }}?
          </v-card-text>
          <v-card-actions>
            <v-btn @click="deleteTeam">Delete Team</v-btn>
            <v-btn @click="deleteDialog = false">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-btn>
    <v-btn size="large" color="red white--text" v-else>Leave Team</v-btn>
  </v-row>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
const { mobile } = useDisplay()

const user = {
  is_admin: true
}

const teamData = {
  team_name: 'CFC Runners',
  total_kilometres: 990,
  invite_code: 'AHGQ234JHGW',
  bio: 'This is our great team bio for our team CFC Runners',
  daily_kms: [],
  sub_teams: [],
  leaderboard: []
}

const editBioDialog = ref(false)
const removeDialog = ref(false)
const deleteDialog = ref(false)
const isBioVisible = ref(false)
const isDailyKmsVisible = ref(false)
const isSubTeamsVisible = ref(false)
const isLeaderboardVisible = ref(false)
const newBioText = ref('')

function copyInviteCode() {
  navigator.clipboard.writeText(teamData.invite_code)
}

const toggleBio = () => {
  isBioVisible.value = !isBioVisible.value
}

const editBio = () => {
  console.log('New Bio:' + newBioText.value)
}

const toggleDailyKms = () => {
  isDailyKmsVisible.value = !isDailyKmsVisible.value
}

const toggleSubTeams = () => {
  isSubTeamsVisible.value = !isSubTeamsVisible.value
}

const toggleLeaderboard = () => {
  isLeaderboardVisible.value = !isLeaderboardVisible.value
}

const deleteTeam = () => {
  console.log('delete team')
  // need to add functionality
}

const deleteTeamMember = () => {
  console.log('delete team member')
  // need to add functionality
}
</script>

<style scoped>
.totalKms {
  color: #009d4f;
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