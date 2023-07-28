<script setup lang="ts">
import { ref, computed, watch, watchEffect } from 'vue'
import type { Ref, PropType } from 'vue'
import ConfirmButton from '@/components/ConfirmButton.vue'
import PopupDialog from '@/components/PopupDialog.vue'
import type { SubteamView, MemberView, UserView } from '@/types/subteam'

// Open dialog, get methods from SubTeams.vue
const emit = defineEmits(['saveSubteam', 'deleteSubTeam', 'update:modelValue'])

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  },
  selectedSubteam: {
    type: Object as PropType<SubteamView>,
    required: true
  },
  availableMemeberList: {
    type: Array as PropType<UserView[]>,
    required: true
  }
})

const isFullscreen = ref(false)

// selectable avaliable member list
const toMemberView = (member: UserView): MemberView => {
  return {
    id: member.id,
    firstName: member.firstName,
    lastName: member.lastName,
    avatar: `/avatars/${member.avatar}`
  }
}

const tmpAvailableSubTeamMembers: Ref<MemberView[]> = ref(
  props.availableMemeberList.map(toMemberView)
)
const tmpSubteamMembers: Ref<MemberView[]> = ref(props.selectedSubteam.members)
const updatedTeamName: Ref<String> = ref(props.selectedSubteam.name)
const selectedMember: Ref<MemberView | null> = ref(null)

watch(
  () => props.selectedSubteam,
  (first) => {
    updatedTeamName.value = JSON.parse(JSON.stringify(first.name))
    tmpSubteamMembers.value = JSON.parse(JSON.stringify(first.members))
  }
)
watch(
  () => props.availableMemeberList,
  (first) => {
    tmpAvailableSubTeamMembers.value = JSON.parse(JSON.stringify(first.map(toMemberView)))
  }
)

//dialog button handler methods
//add a member
const handleAddMemberBtn = () => {
  if (selectedMember.value) {
    tmpSubteamMembers.value.push(selectedMember.value)
    tmpAvailableSubTeamMembers.value = tmpAvailableSubTeamMembers.value.filter(
      (member) => member.id !== selectedMember.value?.id
    )
    selectedMember.value = null
  }
}

//remove a member
const handleRemoveMemberBtn = (memberId: number) => {
  const foundMember: MemberView | undefined = tmpSubteamMembers.value.find(
    (member) => member.id === memberId
  )
  if (foundMember) {
    tmpAvailableSubTeamMembers.value.push(foundMember)
    tmpSubteamMembers.value = tmpSubteamMembers.value.filter((member) => member.id !== memberId)
  }
}

//save subteam
const handleSaveSubteamBtn = () => {
  emit(
    'saveSubteam',
    props.selectedSubteam.subteamId,
    updatedTeamName.value,
    tmpSubteamMembers.value,
    tmpAvailableSubTeamMembers.value
  )
  showDialog.value = false
}

// //delete subteam
const handleRemoveSubteamBtn = () => {
  emit('deleteSubTeam', props.selectedSubteam.subteamId)
  showDialog.value = false
}

const loading = ref(false)
const display = ref(false)
const rules = {
  required: (value: string) => !!value || 'Field is required'
}
const memberId = ref(0)
const showDialog = computed({
  get() {
    return props.modelValue
  },
  set(newValue: boolean) {
    emit('update:modelValue', newValue)
  }
})

watchEffect(async () => {
  const updateFullscreen = async () => {
    isFullscreen.value = window.innerWidth <= 500
  }

  await updateFullscreen()

  window.addEventListener('resize', updateFullscreen)
  return () => {
    window.removeEventListener('resize', updateFullscreen)
  }
})
</script>

<template>
  <!--Edit Subteam-->
  <v-dialog :fullscreen="isFullscreen" max-width="500px" max-height="100vh" v-model="showDialog">
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="emit('update:modelValue', !modelValue)" />
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-6">Edit Subteam</v-card-title>
      <!--Subteam Name-->
      <v-form class="pb-0 mb-0 mx-8">
        <v-text-field
          bg-color="white"
          v-model="updatedTeamName"
          :rules="[rules.required]"
          label="Edit subteam name"
          required
        />
        <v-divider color="info"></v-divider>

        <!--Members-->
        <v-card-title class="justify-center my-2 text-h4">Members</v-card-title>

        <!--Add New Member-->
        <v-select
          :items="tmpAvailableSubTeamMembers"
          label="Select members"
          v-model="selectedMember"
          dense
          @update:modelValue="handleAddMemberBtn"
          bg-color="white"
        >
          <template v-slot:selection="{ item }">
            <v-list-item
              v-bind="item"
              :title="item.raw.firstName + ' ' + item.raw.lastName"
            ></v-list-item>
          </template>
          <template v-slot:item="{ props, item }">
            <v-list-item
              v-bind="props"
              :prepend-avatar="item.raw.avatar"
              :title="item.raw.firstName + ' ' + item.raw.lastName"
            />
            <v-divider color="info"></v-divider>
          </template>
        </v-select>

        <!--Member List-->
        <v-list v-if="tmpSubteamMembers.length != 0" class="bg-backgroundGrey">
          <v-list-item v-for="(member, index) in tmpSubteamMembers" :key="index">
            <v-avatar>
              <img :src="member.avatar" alt="Avatar" class="custom-avatar" />
            </v-avatar>
            <span class="ml-3 font-weight-bold">
              {{ member.firstName + ' ' + member.lastName }}
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
              @handle-submit="handleRemoveMemberBtn(memberId)"
            />
            <v-divider class="mt-4" color="info"></v-divider>
          </v-list-item>
        </v-list>
        <v-row v-else justify="center" class="mb-4">No members attached to subteam</v-row>
        <!--Buttons-->
        <v-card-actions class="justify-center mb-4">
          <div class="w-100 d-flex justify-center">
            <v-btn color="secondaryGreen" class="mr-8" variant="flat" @click="handleSaveSubteamBtn"
              >Save</v-btn
            >
            <ConfirmButton
              :action="'delete'"
              :object="'subteam'"
              :use-done-for-button="false"
              :loading="loading"
              @handle-confirm="handleRemoveSubteamBtn"
            />
          </div>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<style scoped>
.v-list-item {
  padding: 4px 10px !important;
}

.custom-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.v-list__input:hover {
  background-color: #ff0000 !important;
}

.v-input.custom-text-field input {
  font-size: 48px !important;
}
</style>
