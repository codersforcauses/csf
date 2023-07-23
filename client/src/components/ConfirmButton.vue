<script setup lang="ts">
import { ref } from 'vue'
import PopupDialog from './PopupDialog.vue'
import { capitalize } from 'vue'

const emit = defineEmits(['handleConfirm'])
const props = defineProps<{
  action: string
  object: string
  useDoneForButton?: boolean
  loading: boolean
}>()

const display = ref(false)
</script>

<template>
  <!-- u may wanna may the class a prop so the button can be styled differently as needed -->
  <v-btn class="bg-primaryRed" @click="display = true">
    <PopupDialog
      v-model="display"
      :title="'Confirm ' + capitalize(`${props.object} ${props.action}`)"
      :text="`Are you sure you wish to ${props.action} this ${props.object}?`"
      :submit-text="capitalize(props.action)"
      @handle-submit="() => emit('handleConfirm')"
    />
    <v-progress-circular v-if="loading" indeterminate size="24" color="white"></v-progress-circular>
    <span v-else> {{ props.useDoneForButton ? 'DONE' : props.action.toUpperCase() }}</span>
  </v-btn>
</template>
