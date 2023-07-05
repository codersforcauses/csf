<template>
  <v-dialog fullscreen>
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover></v-img>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-icon icon="mdi-close" size="x-large" @click="closeModal"></v-icon>
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-5">{{
        type === 'Create' ? 'Create Event' : 'Edit Event'
      }}</v-card-title>
      <v-text-field hide-details bg-color="white" label="Event Name" v-model="name" class="mx-5"></v-text-field>
      <v-text-field hide-details bg-color="white" label="Start Date" type="date" v-model="startDate"
        class="mx-5"></v-text-field>
      <v-text-field hide-details bg-color="white" label="End Date" type="date" v-model="endDate"
        class="mx-5"></v-text-field>
      <v-textarea hide-details bg-color="white" label="Description" v-model="description" class="mx-5"></v-textarea>
      <v-card-actions v-if="type === 'Edit'" class="justify-center mb-4">
        <v-btn variant="outlined" class="text-secondaryBlue mr-16 " @click="archiveEvent">ARCHIVE</v-btn>
        <v-btn class="bg-primaryRed" @click="editEvent">DONE</v-btn>
        <v-btn variant="outlined" class="text-primaryRed ml-16" @click="deleteEvent">DELETE</v-btn>
      </v-card-actions>
      <v-card-actions v-else class="justify-center mb-4">
        <v-btn class="bg-primaryRed" @click="addEvent">DONE</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { type Event } from '../types/event'
import { useEventStore } from '../stores/event';
const props = defineProps<{ type: 'Create' | 'Edit'; event?: Event }>()
const emit = defineEmits(['close'])
const eventStore = useEventStore();

const name = ref(props.event ? props.event.name : '')
const startDate = ref(props.event ? props.event.startDate : '')
const endDate = ref(props.event ? props.event.endDate : '')
const description = ref(props.event ? props.event.description : '')

const addEvent = async () => {
  try {
    await eventStore.createEvent(name.value, startDate.value, endDate.value, description.value);
  } catch (error) {
    console.log(error);
    return;
  }
  closeModal()
}

const editEvent = async () => {
  try {
    if (props.event) {
      await eventStore.editEvent(props.event.eventId, name.value, startDate.value, endDate.value, description.value, props.event.isPublic, props.event.isArchived);
    }
  } catch (error) {
    console.log(error);
    return;
  }
  closeModal()
}

const archiveEvent = async () => {
  try {
    if (props.event) {
      await eventStore.editEvent(props.event.eventId, name.value, startDate.value, endDate.value, description.value, props.event.isPublic, true);
    }
  } catch (error) {
    console.log(error);
    return;
  }
  closeModal()
}

const deleteEvent = async () => {
  try {
    if (props.event)
      await eventStore.deleteEvent(props.event.eventId);

  } catch (error) {
    console.log(error);
    return;
  }
  closeModal();
}

function closeModal() {
  emit('close')
}
</script>
