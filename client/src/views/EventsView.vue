<template>
  <div v-if="!isLoading">
    <v-row
      class="bg-primaryWhite pt-6 mx-3"
      align="center"
      no-gutters
      v-if="filteredEventsList.length != 0"
    >
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
      <div v-if="filteredEventsList.length == 0" class="mt-6 mx-3 text-center">
        <v-icon icon="mdi-calendar-blank" size="x-large" />
        <p class="font-weight-bold text-body-1 mt-3">No current events :(</p>
        <v-btn
          v-if="tempIsTeamAdmin"
          size="x-large"
          class="bg-primaryRed text-primaryWhite mt-3"
          @click="isAddingEvent = true"
          >ADD EVENT
        </v-btn>
      </div>
    </div>
  </div>
  <div v-else class="w-100 d-inline-block">
    <v-progress-circular indeterminate color="primaryRed" class="mt-12 mx-auto d-block" />
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
const isLoading = ref(true)

onMounted(async () => {
  await eventStore.getEvents()
  isLoading.value = false
})

const searchQuery = ref('')
const filteredEventsList = computed<Event[]>(() =>
  eventStore.events.filter((e) =>
    (e.name + e.description).toLowerCase().includes(searchQuery.value)
  )
)
const tempIsTeamAdmin = ref<boolean>(true)
const isAddingEvent = ref<boolean>(false)
const isEditingEvent = ref<boolean>(false)
const editingEvent = ref<Event>(<Event>{})

const closeModal = () => {
  isAddingEvent.value = false
  isEditingEvent.value = false
}

function openEditModal(id: number) {
  let foundEvent = eventStore.events.find((e) => e.eventId === id)
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
