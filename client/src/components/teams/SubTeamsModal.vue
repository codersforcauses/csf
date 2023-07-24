<script setup lang="ts">
import { ref, computed, watch } from 'vue'
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

// selectable avaliable member list
const toMemberView = (member: UserView): MemberView => {
  return {
    id: member.id,
    firstName: member.firstName,
    lastName: member.lastName,
    // todo change to public folder
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
            v-model="updatedTeamName"
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
          :items="tmpAvailableSubTeamMembers"
          label="Select member"
          v-model="selectedMember"
          dense
          @update:modelValue="handleAddMemberBtn"
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
        <v-list>
          <v-list-item v-for="(member, index) in tmpSubteamMembers" :key="index">
            <v-list-item-content>
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
            </v-list-item-content>
            <v-divider class="mt-4" color="info"></v-divider>
          </v-list-item>
        </v-list>
        <!--Buttons-->
        <div class="w-100 d-flex justify-center">
          <v-btn color="secondaryGreen" class="mr-8" variant="flat" @click="handleSaveSubteamBtn"
            >Save</v-btn
          >
          <ConfirmButton
            :action="'delete'"
            :object="'subteam'"
            :use-done-for-button="false"
            @handle-confirm="handleRemoveSubteamBtn"
          />
        </div>
      </v-card-text>
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

.v-input.custom-text-field input {
  font-size: 48px !important;
}
</style>
