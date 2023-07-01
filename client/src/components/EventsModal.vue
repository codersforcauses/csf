<template>
  <v-dialog fullscreen>
      <v-card color="#ECECEC">
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-icon class="me-1" icon="mdi-close" @click="closeModal"></v-icon>
        </v-card-actions>
        <v-card-title class="justify-center text-h4">{{ type === 'Create' ? 'Create Event' : 'Edit Event' }}</v-card-title>
        <v-text-field hide-details bg-color="white" placeholder="Event Name" v-model="name"></v-text-field>
        <v-text-field hide-details bg-color="white" placeholder="Start Date" type="date" v-model="startDate"></v-text-field>
        <v-text-field hide-details bg-color="white" placeholder="End Date" type="date" v-model="endDate"></v-text-field>
        <v-textarea hide-details bg-color="white" placeholder="Description" v-model="description"></v-textarea> 
        <v-card-actions v-if="type === 'Edit'" class="justify-center">
          <v-btn variant="outlined" class="text-secondaryBlue mr-16"  @click="archiveEvent">ARCHIVE</v-btn>
          <v-btn class="bg-primaryRed ml-16" @click="editEvent">DONE</v-btn>
        </v-card-actions>
        <v-card-actions v-else class="justify-center">
          <v-btn class="bg-primaryRed" @click="addEvent">DONE</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
    import { ref } from 'vue'
    interface Props {
        type: "Create" | "Edit"
        id?: number
        orignalName?: string
        originalStartDate?: string
        originalEndDate?: string
        originalDescription?: string
    }
    const props = defineProps<Props>()
    const emit = defineEmits(['close'])
  
    const name = ref(props.orignalName)
    const startDate = ref(props.originalStartDate)
    const endDate = ref(props.originalEndDate)
    const description = ref(props.originalDescription)
  
    function addEvent() {
      console.log("Contact backend to add the event", name.value, startDate.value, endDate.value, description.value)
      closeModal()
    }
  
    function editEvent() {
      console.log("Contact backend to edit the event", props.id, name.value, startDate.value, endDate.value, description.value)
      closeModal()
    }
  
    function archiveEvent() {
      console.log("Contact backend to archive the event", props.id)
      closeModal()
    }
  
    function closeModal() {
        emit('close')
    }
  </script>