<script setup lang="ts">
import { ref, reactive, toRef, computed, watch } from 'vue'
import type { Ref, PropType } from 'vue'

import ConfirmButton from '@/components/ConfirmButton.vue'
import PopupDialog from '@/components/PopupDialog.vue'

import type { SubteamView, MemberView } from '@/types/subteam'

// Open dialog, get methods from SubTeams.vue
const emit = defineEmits(['saveTeam', 'removeSubTeam', 'update:modelValue'])

const props = defineProps({
  selectedSubteam: {
    type: Object as PropType<SubteamView>,
    required: true
  },
  modelValue: {
    type: Boolean,
    required: true
  },
  availableMemeberList: {
    type: Array as PropType<MemberView[]>,
    required: true
  }
})

let selectedSubteamCopy: SubteamView = reactive({
  name: '',
  teamId: 0,
  subteamId: 0,
  totalKm: '',
  members: [
    {
      id: 13,
      firstname: 'Unknown',
      lastname: 'Unknown',
      avatar: 'https://cdn.vuetifyjs.com/images/john.png'
    }
  ]
})

//Modify selectedSubteam Copy
watch(
  () => props.selectedSubteam,
  (first) => {
    //local selectedTeam Copy to change values
    selectedSubteamCopy = reactive({
      name: first.name,
      teamId: first.teamId,
      subteamId: first.subteamId,
      totalKm: first.totalKm,
      members: first.members
    })
  }
)

// edit sub team name input rules
const rules = {
  required: (value: string) => !!value || 'Field is required'
}

//avaliable member list
const avaliableMemeberList: Ref<MemberView[]> = toRef(props, 'avaliableMemeberList')
const selectedMember: Ref<MemberView> = ref({
  id: 0,
  firstname: '',
  lastname: '',
  avatar: ''
})

const addMember = () => {
  if (selectedMember.value !== null) {
    selectedSubteamCopy.members.push(selectedMember.value)
    // Removing that member from the avaliable members drop down list
    for (let i = 0; i < avaliableMemeberList.value.length; i++) {
      if (avaliableMemeberList.value[i].id === selectedMember.value.id) {
        avaliableMemeberList.value.splice(i, 1)
      }
    }
    // Setting selected member to null
    selectedMember.value = {
      id: 0,
      firstname: '',
      lastname: '',
      avatar: ''
    }
  }
}

const removeMember = (memberId: number) => {
  // Find the member to be removed
  const foundMember: MemberView | undefined = selectedSubteamCopy.members.find(
    (item) => item.id === memberId
  )

  // If found, add it to the avaliable member list and remove it from the selected subteam
  if (foundMember) {
    avaliableMemeberList.value.push(foundMember)
    selectedSubteamCopy.members = selectedSubteamCopy.members.filter((item) => item.id !== memberId)
  }
}

const display = ref(false)
const memberId = ref(0)

const showDialog = computed({
  // getter
  get() {
    return props.modelValue
  },
  // setter
  set(newValue: boolean) {
    // Note: we are using destructuring assignment syntax here.
    emit('update:modelValue', newValue)
  }
})
</script>

<template>
  <!--Edit Subteam-->
  <v-dialog v-model="showDialog" fullscreen transition="dialog-bottom-transition">
    <v-img src="/images/Footer-min.jpeg" width="100%" max-height="32" cover />
    <v-card>
      <v-card-text>
        <!--Subteam Name-->
        <v-btn
          class="ma-0 pa-0 float-right"
          variant="text"
          icon="mdi mdi-window-close"
          @click="emit('update:modelValue', !modelValue)"
        />
        <div class="font-weight-bold my-6 text-h4">Edit Subteam</div>
        <div class="w-100 d-flex flex-column text-center align-center justify-center">
          <v-text-field
            variant="solo"
            v-model="selectedSubteamCopy.name"
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
          :items="avaliableMemeberList"
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
          <v-list-item v-for="(member, index) in selectedSubteamCopy.members" :key="index">
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
                @click="
                  () => {
                    display = true
                    memberId = member.id
                  }
                "
              />
              <PopupDialog
                v-model="display"
                :title="'Remove Team Member'"
                :text="`Are you sure you wish to remove this member?`"
                :submit-text="'Confirm'"
                @handle-submit="removeMember(memberId)"
              />
            </v-list-item-content>
            <v-divider class="mt-4" color="info"></v-divider>
          </v-list-item>
        </v-list>
        <!--Buttons-->
        <div class="w-100 d-flex justify-center">
          <v-btn
            color="success"
            class="mr-8"
            variant="flat"
            @click="$emit('saveTeam', selectedSubteamCopy, avaliableMemeberList)"
            >Save</v-btn
          >
          <ConfirmButton
            :action="'delete'"
            :object="'subteam'"
            :use-done-for-button="false"
            @handle-confirm="$emit('removeSubTeam', selectedSubteam.teamId)"
          />
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
