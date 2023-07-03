<template>
  <v-row class="bg-primaryWhite pl-4 pt-4" align="center" no-gutters>
    <v-col>
      <v-text-field
      prepend-inner-icon="mdi-magnify"
      hide-details
      placeholder="Search Events"
      clearable
      v-model="searchQuery"
    />
    </v-col>
    <v-col class="justify-center d-flex" cols="2">
      <v-btn
        v-if="tempIsTeamAdmin"
        size="x-large"
        density="compact"
        icon="mdi-plus"
        class="bg-primaryRed text-primaryWhite"
        @click="isAddingEvent = true"
      >
      </v-btn>
    </v-col>
  </v-row>
  <div id="cards-container" class="bg-primaryWhite pt-4">
    <Event
      v-for="event in filteredEventsList"
      key="event.id"
      :event="event"
      :isTeamAdmin="tempIsTeamAdmin"
      @edit="openEditModal"
    />
  </div>
  <EventsModal v-if="isAddingEvent" :type="'Create'" @close="closeModal" v-model="isAddingEvent"></EventsModal>
  <EventsModal
    v-if="isEditingEvent"
    :type="'Edit'"
    :event="editingEvent"
    @close="closeModal"
    v-model="isEditingEvent"
  ></EventsModal>
</template>

<script setup lang="ts">
import Event from '../components/Event.vue'
import EventsModal from '../components/EventsModal.vue'
import { ref, computed } from 'vue'

interface Event {
  id: number
  name: string
  startDate: string
  endDate: string
  description: string
  isPrivate: boolean
}

const temporaryEventsList = ref<Event[]>([
  {
    id: 1,
    name: 'Run Very Far',
    startDate: '2023-11-14',
    endDate: '2023-11-15',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
    isPrivate: false
  },
  {
    id: 2,
    name: 'Run Even Further',
    startDate: '2023-10-14',
    endDate: '2023-10-19',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
    isPrivate: true
  },
  {
    id: 3,
    name: 'Walk',
    startDate: '2023-11-22',
    endDate: '2023-11-29',
    description:
      'Designers use Lorem Ipsum as a dummy text, something to cover the fact that content is missing from the wireframe. “Lorem Ipsum” is followed by more Latin text, making it easy for users or other designers to ignore it and imagine something more familiar or relevant in its place.',
    isPrivate: true
  },
  {
    id: 4,
    name: 'Walk again',
    startDate: '2023-11-12',
    endDate: '2023-11-12',
    description: 'walk again!',
    isPrivate: false
  }
])
const searchQuery = ref<string>('')
const filteredEventsList = computed<Event[]>(() => {
  let query: string = searchQuery.value ? searchQuery.value.toLowerCase() : ''
  return temporaryEventsList.value.filter(
    (e) =>
      e.name.toLowerCase().includes(query) ||
      e.description.toLowerCase().includes(searchQuery.value)
  )
})
const tempIsTeamAdmin = ref<boolean>(true)
const isAddingEvent = ref<boolean>(false)
const isEditingEvent = ref<boolean>(false)
const editingEvent = ref<Event>(<Event>{})

function closeModal() {
  isAddingEvent.value = false;
  isEditingEvent.value = false;
}

function openEditModal(id: number) {
  let foundEvent = filteredEventsList.value.find((e) => e.id === id)
  if (foundEvent) {
    editingEvent.value = foundEvent
    isEditingEvent.value = true
  }
}
</script>

<style>
#cards-container > .v-card:nth-child(odd) {
  background-color: #f4f4f4;
}
</style>
