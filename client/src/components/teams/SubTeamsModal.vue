<script setup lang="ts">
import { ref, reactive, toRef, computed, watch} from 'vue'
import type { Ref, PropType} from 'vue';

import ConfirmButton from '@/components/ConfirmButton.vue'
import PopupDialog from '@/components/PopupDialog.vue'

//create interferences for member and selectedTeam Object
interface Member {
  id: number;
  firstname: string;
  lastname: string;
  avatar: string;
}

//TODO SUBTEAM
interface Team {
    teamName: string;
    teamId: string;
    totalKM: string;
    members: Member[];
}

// Open dialog
const emit = defineEmits(['saveTeam', 'removeSubTeam', 'controlDialog'])

const props = defineProps({
  selectedTeam: {
      type: Object as PropType<Team>,
      required: true
  },
  dialog: {
    type: Boolean,
    required: true
  },
  //AvaliableMemeberList
  noTeamMembers: {
        type: Array as PropType<Member[]>,
        required: true
  }
})

//Modify selectedTeam
watch(() => props.selectedTeam, (first, second) => {
    //local selectedTeam -> Local
    _selectedTeam = reactive({
        teamName: first.teamName,
        teamId: first.teamId,
        totalKM: first.totalKM,
        members: first.members
    })
    updatedTeamName.value = props.selectedTeam.teamName
});

 
// edit sub team name input rules
const rules = {
    required: (value: string) => !!value || 'Field is required'
}

const updatedTeamName: Ref<String> = ref(props.selectedTeam?.teamName)


// selectable avaliable member list
const noTeamMembers: Ref<Member[]> = toRef(props, 'noTeamMembers')
const selectedMember: Ref<Member> = ref({
    id: 0,
    firstname: '',
    lastname: '',
    avatar: ''
})

const addMember = () => {
    if (selectedMember.value !== null) {
        _selectedTeam.members.push(selectedMember.value)
        // Removing that member from the select members drop down list
        for (let i = 0; i < noTeamMembers.value.length; i++) {
            if (noTeamMembers.value[i].id === selectedMember.value.id) {
                noTeamMembers.value.splice(i, 1)
            }
        }

        console.log(noTeamMembers.value);

        // Setting selected member to null
        selectedMember.value = {
            id: 0,
            firstname: '',
            lastname: '',
            avatar: ''
        }
    }
}

// members in team

let _selectedTeam :Team= reactive({
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
})

const removeMember = (memberId: number) => {
  // // Find the member that was removed
  const foundMember: Member | undefined = _selectedTeam.members.find((item) => item.id === memberId)
  // // // Add them to the all members list
  if (foundMember) {
  noTeamMembers.value.push(foundMember);
  _selectedTeam.members = _selectedTeam.members.filter((item) => item.id !== memberId)

}
}

const display = ref(false)

//dummy data
const _dialog = computed({
    // getter
    get() {
        return props.dialog
    },
    // setter
    set(newValue: boolean) {
        // Note: we are using destructuring assignment syntax here.
        emit('controlDialog', newValue)
    }
})
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
            v-model="_selectedTeam.teamName"
            :rules="[rules.required]"
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
          :items="noTeamMembers"
          label="Select member"
          v-model="selectedMember"
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
          <v-list-item v-for="(member, index) in _selectedTeam.members" :key="index">
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
          <v-btn color="success" class="mr-8" variant="flat" @click="$emit('saveTeam', _selectedTeam, noTeamMembers)">Save</v-btn>
          <ConfirmButton
            :action="'delete'"
            :object="'subteam'"
            :use-done-for-button="false"
            @handle-confirm="$emit('removeSubTeam', selectedTeam.teamId)"
          />
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
