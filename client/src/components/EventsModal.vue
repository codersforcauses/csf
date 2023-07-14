<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import { type Event } from '../types/event'
import { useEventStore } from '../stores/event'
import ConfirmButton from '@/components/ConfirmButton.vue'

const props = defineProps<{ type: 'Create' | 'Edit'; event?: Event }>()
const emit = defineEmits(['close'])
const eventStore = useEventStore()

const name = ref(props.event?.name ?? '')
const startDate = ref(props.event?.startDate ?? '')
const endDate = ref(props.event?.endDate ?? '')
const description = ref(props.event?.description ?? '')
const isPublic = ref(props.event?.isPublic ?? false)
const isFullscreen = ref(false)

const refs = () => ({
  name: name.value,
  startDate: startDate.value,
  endDate: endDate.value,
  description: description.value,
  isPublic: isPublic.value
})

const addEvent = () => eventStore.createEvent(refs()).then(closeModal).catch(console.log)

const editEvent = () => {
  if (props.event)
    return eventStore
      .editEvent({
        ...props.event,
        ...refs()
      })
      .then(closeModal)
      .catch(console.log)
}

const archiveEvent = () => {
  if (props.event)
    return eventStore
      .editEvent({
        ...props.event,
        ...refs(),
        isArchived: true
      })
      .then(closeModal)
      .catch(console.log)
}

const deleteEvent = () => {
  if (props.event)
    return eventStore.deleteEvent(props.event.eventId).then(closeModal).catch(console.log)
}

const closeModal = () => emit('close')

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
  <v-dialog :fullscreen="isFullscreen" max-width="500px" max-height="100vh">
    <v-card class="bg-backgroundGrey">
      <v-img src="/images/Footer-min.jpeg" width="100%" max-height="16" cover />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="closeModal" />
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-6">{{ `${type} Event` }}</v-card-title>
      <form class="pb-0 mb-0 mx-8">
        <v-text-field bg-color="white" label="Event Name" v-model="name" class="mx-5" />
        <v-text-field
          bg-color="white"
          label="Start Date"
          type="date"
          v-model="startDate"
          class="mx-5"
        />
        <v-text-field
          bg-color="white"
          label="End Date"
          type="date"
          v-model="endDate"
          class="mx-5"
        />
        <v-textarea bg-color="white" label="Description" v-model="description" class="mx-5" />
        <v-card-actions v-if="type === 'Edit'" class="justify-center mb-4">
          <v-btn variant="outlined" class="text-secondaryBlue mr-16" @click="archiveEvent"
            >ARCHIVE</v-btn
          >
          <ConfirmButton
            :action="'edit'"
            :object="'event'"
            :use-done-for-button="true"
            @handle-confirm="editEvent"
          />
          <v-btn variant="outlined" class="text-primaryRed ml-16" @click="deleteEvent"
            >DELETE</v-btn
          >
        </v-card-actions>
        <v-card-actions v-else class="justify-center mb-4">
          <ConfirmButton
            :action="'create'"
            :object="'event'"
            :use-done-for-button="true"
            @handle-confirm="addEvent"
          />
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>
