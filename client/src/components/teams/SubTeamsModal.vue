<script setup lang="ts">
import { ref, reactive, toRefs,onMounted,computed,PropType } from 'vue'

import ConfirmButton from '@/components/ConfirmButton.vue'
import PopupDialog from '@/components/PopupDialog.vue'


interface Member {
  id: number;
  firstname: string;
  lastname: string;
  avatar: string;
}

interface SelectedTeam {
  teamName: string;
  teamId: string;
  totalKM: string;
  members: Member[];
}

 
// control dialog, save team
const emit = defineEmits(['saveTeam', 'removeSubTeam','updateAllMembers','controlDialog'])
const props = defineProps({
  selectedTeam: {
            type: Object as PropType<SelectedTeam>,
            required: true
        },
        dialog: {
          type: Boolean,
          required: true
        },
        allMembers: {
          type: Array as PropType<Member[]>,
          required: true
        }
    })
 
 
onMounted(() => {
  data.updatedTeamName = props.selectedTeam.teamName
  data.allMembers = props.allMembers 
})
 

const display = ref(false)

//dummy data
const data = reactive({

  selectedMember  : null,
  allMembers:{},
  
  rules: {
    required: (value: string) => !!value || 'Field is required'
  },
 
  // selectedTeam: {
  //   teamName: '',
  //   teamId: '',
  //   totalKM: '',
  //   members: [
  //     {
  //       id: 13,
  //       firstname: 'Tom',
  //       lastname: 'T',
  //       avatar: 'https://cdn.vuetifyjs.com/images/john.png'
  //     }
  //   ]
  // },
  // allMembers:
  updatedTeamName: ''
})
 
const _dialog = computed({
  // getter
  get() {
    return props.dialog
  },
  // setter
  set(newValue) {
    // Note: we are using destructuring assignment syntax here.

    emit('controlDialog', newValue)
  }
})
// methods
const removeMember = (memberId: number) => {
  // // Find the member that was removed
  const foundMember = data.selectedTeam.members.filter((item) => item.id === memberId)[0]
  // // Add them to the all members list
  allMembers.push(foundMember)

  data.selectedTeam.members = data.selectedTeam.members.filter((item) => item.id !== memberId)
}
const addMember = () => {
  if (data.selectedMember) {
    data.selectedTeam.members.push(data.selectedMember)
    // Removing that member from the select members drop down list
   const tempAllMembers= data.allMembers.filter((member) => member !== data.selectedMember)
    emit('updateAllMembers',tempAllMembers)
    // Setting selected member to null
    data.selectedMember = null
  }
}
// -----------------------------
</script>

<template>
  <!--Edit Subteam-->
  <v-dialog v-model="_dialog" fullscreen transition="dialog-bottom-transition">
    <v-img src="/images/Footer-min.jpeg" width="100%" max-height="32" cover />
    <v-card>
      <v-card-text>
        <!--Subteam Name-->
        <v-btn
          class="ma-0 pa-0 float-right"
          variant="text"
          icon="mdi mdi-window-close"
          @click="emit('controlDialog', false)"
        />
        <div class="font-weight-bold my-6 text-h4">Edit Subteam</div>
        <div class="w-100 d-flex flex-column text-center align-center justify-center">
          <v-text-field
            variant="solo"
            v-model="data.updatedTeamName"
            :rules="[data.rules.required]"
            label="Edit subteam name"
            required
            dense
            class="text-h3 w-75 py-3 custom-text-field"
          />
        </div>
        <v-divider class="my-4" color="info"></v-divider>

        <!--Members-->
        <div class="font-weight-bold my-6 text-h4">Members</div>

        <!--Add New Member-->
        <v-select
          :items="allMembers"
          label="Select member"
          v-model="data.selectedMember"
          dense
          @update:modelValue="addMember"
        >
          <template v-slot:selection="{ item }">
            <v-list-item
              v-bind="item"
              :title="item.raw.firstname + ' ' + item.raw.lastname"
            ></v-list-item>
          </template>
          <template v-slot:item="{ props, item }">
            <v-list-item
              v-bind="props"
              prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
              :title="item.raw.firstname + ' ' + item.raw.lastname"
            />
            <v-divider color="info"></v-divider>
          </template>
        </v-select>

        <!--Member List-->
        <v-list>
          <v-list-item v-for="(member, index) in data.selectedTeam?.members" :key="index">
            <v-list-item-content>
              <v-avatar>
                <img :src="member.avatar" alt="Avatar" class="custom-avatar" />
              </v-avatar>
              <span class="ml-3 font-weight-bold">
                {{ member.firstname + ' ' + member.lastname }}
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
            @handle-confirm="emit('removeSubTeam', selectedTeam.teamId)"
          />
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
