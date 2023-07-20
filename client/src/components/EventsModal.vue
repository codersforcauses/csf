<script setup lang="ts">
import { ref, watchEffect, reactive } from 'vue'
import { type Event, type EventError } from '../types/event'
import { useEventStore } from '../stores/event'
import ConfirmButton from '@/components/ConfirmButton.vue'
import { notify } from '@kyvg/vue3-notification'
import { AxiosError } from 'axios'
import camelize from 'camelize-ts'

const props = defineProps<{ type: 'Create' | 'Edit'; event?: Event }>()
const emit = defineEmits(['close'])
const eventStore = useEventStore()

const name = ref(props.event?.name ?? '')
const startDate = ref(props.event?.startDate ?? '')
const endDate = ref(props.event?.endDate ?? '')
const description = ref(props.event?.description ?? '')
const isPublic = ref(props.event?.isPublic ?? false)
const isFullscreen = ref(false)
const valid = ref(true)

const refs = () => ({
  name: name.value,
  startDate: startDate.value,
  endDate: endDate.value,
  description: description.value,
  isPublic: isPublic.value
})

const errors = reactive<EventError>({
  name: [],
  startDate: [],
  endDate: [],
  description: [],
})

const required = (v: string) => !!v || 'Field is required'

const addEvent = () => {
  eventStore
  .createEvent(refs())
  .then(() => {
    notify({
      title: 'Add Event',
      type: 'success',
      text: 'Add Event Successful'
    })
    closeModal()
  })
  .catch((error: AxiosError | any) => {
    if (error instanceof AxiosError && error.response && error.response.status === 400) {
      let newErrors = camelize(error.response.data) as unknown as EventError
      if (newErrors.nonFieldErrors) {
        errors.startDate = newErrors.nonFieldErrors
      }
    }
    notify({
      title: 'Add Event',
      type: 'error',
      text: 'Error adding event'
    })
  })
}
  

const editEvent = () => {
  if (props.event)
    return eventStore
      .editEvent({
        ...props.event,
        ...refs()
      })
      .then(() => {
        notify({
          title: 'Edit Event',
          type: 'success',
          text: 'Edit Event Successful'
        })
        closeModal()
      })
      .catch((error: AxiosError | any) => {
        if (error instanceof AxiosError && error.response && error.response.status === 400) {
          let newErrors = camelize(error.response.data) as unknown as EventError
          if (newErrors.nonFieldErrors) {
            errors.startDate = newErrors.nonFieldErrors
          }
        }
        notify({
          title: 'Edit Event',
          type: 'error',
          text: 'Edit Event Error'
        })
      })
}

const archiveEvent = () => {
  if (props.event)
    return eventStore
      .editEvent({
        ...props.event,
        ...refs(),
        isArchived: true
      })
      .then(() => {
        notify({
          title: 'Archive Event',
          type: 'success',
          text: 'Archive Event Successful'
        })
        closeModal()
      })
      .catch(() => {
        notify({
          title: 'Archive Event',
          type: 'error',
          text: 'Archive Event Error'
        })
      })
}

const deleteEvent = () => {
  if (props.event)
    return eventStore
      .deleteEvent(props.event.eventId)
      .then(() => {
        notify({
          title: 'Delete Event',
          type: 'success',
          text: 'Delete Event Successful'
        })
        closeModal()
      })
      .catch(() => {
        notify({
          title: 'Delete Event',
          type: 'error',
          text: 'Delete Event Error'
        })
      })
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
      <v-img
        src="/images/Footer-min.jpeg"
        width="100%"
        max-height="16"
        alt="red background"
        cover
      />
      <v-card-actions>
        <v-spacer />
        <v-icon icon="mdi-close" size="x-large" @click="closeModal" />
      </v-card-actions>
      <v-card-title class="justify-center text-h4 mb-6">{{ `${type} Event` }}</v-card-title>
      <v-form class="pb-0 mb-0 mx-8" v-model="valid">
        <v-text-field bg-color="white" label="Event Name" v-model="name" class="mx-5" :rules="[required]"/>
        <v-text-field
          bg-color="white"
          label="Start Date"
          type="date"
          :rules="[required]"
          v-model="startDate"
          :error-messages="errors.startDate"
          @focus="errors.startDate = []"
          class="mx-5"
        />
        <v-text-field
          bg-color="white"
          label="End Date"
          type="date"
          :rules="[required]"
          v-model="endDate"
          class="mx-5"
        />
        <v-textarea bg-color="white" label="Description" v-model="description" :rules="[required]" class="mx-5" />
        <v-card-actions v-if="type === 'Edit'" class="justify-center mb-4">
          <v-btn variant="outlined" class="text-secondaryBlue mr-16" @click="archiveEvent"
            >ARCHIVE</v-btn
          >
          <ConfirmButton
            :action="'edit'"
            :object="'event'"
            :disabled="!valid"
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
            :disabled="!valid"
            :use-done-for-button="true"
            @handle-confirm="addEvent"
          />
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>
