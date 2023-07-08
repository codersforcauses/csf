<template>
  <div v-if="!isLoading">
    <v-row class="bg-primaryWhite pt-6 mx-3" align="center" no-gutters>
      <v-text-field
        prepend-inner-icon="mdi-magnify"
        hide-details
        variant="outlined"
        placeholder="Search Events"
        class="mr-3"
        clearable
        v-model="searchQuery"
      />
      <v-btn
        v-if="tempIsTeamAdmin"
        size="x-large"
        density="compact"
        variant="flat"
        icon="mdi-plus"
        class="bg-primaryRed text-primaryWhite"
        @click="isAddingEvent = true"
      >
      </v-btn>
    </v-row>
    <div id="cards-container" class="bg-primaryWhite pt-4">
      <EventCard
        v-for="event in filteredEventsList"
        :key="event.eventId"
        :event="event"
        :isTeamAdmin="tempIsTeamAdmin"
        @edit="openEditModal"
      />
    </div>
  </div>
  <EventsModal v-if="isAddingEvent" :type="'Create'" @close="closeModal" v-model="isAddingEvent" />
  <EventsModal
    v-if="isEditingEvent"
    :type="'Edit'"
    :event="editingEvent"
    @close="closeModal"
    v-model="isEditingEvent"
  />
</template>

<script setup lang="ts">
import EventCard from '../components/EventCard.vue'
import { type Event } from '../types/event'
import EventsModal from '../components/EventsModal.vue'
import { ref, computed, onMounted } from 'vue'
import { useEventStore } from '../stores/event'

const eventStore = useEventStore()
const isLoading = ref<boolean>(true)
const eventList = ref()

onMounted(async () => {
  try {
    await eventStore.getEvents()
    eventList.value = eventStore.events
  } catch (error) {
    console.log(error)
  }
  console.log(eventList.value)
  isLoading.value = false
})

const searchQuery = ref<string>('')
const filteredEventsList = computed<Event[]>(() => {
  let query: string = searchQuery.value ? searchQuery.value.toLowerCase() : ''
  return eventList.value.filter(
    (e: Event) =>
      e.name.toLowerCase().includes(query) ||
      e.description.toLowerCase().includes(searchQuery.value)
  )
})
const tempIsTeamAdmin = ref<boolean>(true)
const isAddingEvent = ref<boolean>(false)
const isEditingEvent = ref<boolean>(false)
const editingEvent = ref<Event>(<Event>{})

const closeModal = () => {
  isAddingEvent.value = false
  isEditingEvent.value = false
}

function openEditModal(id: number) {
  let foundEvent = eventList.value.find((e: Event) => e.eventId === id)
  if (foundEvent) {
    editingEvent.value = foundEvent
    isEditingEvent.value = true
  }
}
</script>

<style scoped>
#cards-container > .v-card:nth-child(odd) {
  background-color: #f4f4f4;
}

.v-field__input {
  padding-top: 19px;
  padding-bottom: 0px;
  margin-top: -19px;
}
</style>
