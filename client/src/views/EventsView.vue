<template>
  <v-container v-if="!isLoading">
    <v-row
      class="bg-primaryWhite pt-6 mx-3"
      align="center"
      no-gutters
      v-if="eventStore.events.length != 0"
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
        v-if="user?.teamAdmin"
        size="x-large"
        density="compact"
        variant="flat"
        icon="mdi-plus"
        class="bg-primaryRed text-primaryWhite"
        @click="isAddingEvent = true"
      >
      </v-btn>
    </v-row>
    <div id="cards-container" class="pt-4">
      <EventCard
        v-for="(event, idx) in filteredEventsList"
        :key="event.eventId"
        :event="event"
        @edit="openEditModal"
        :background-colour="idx % 2 === 0 ? 'bg-primaryWhite' : 'bg-backgroundGrey'"
      />
      <div v-if="filteredEventsList.length == 0" class="mt-6 mx-3 text-center">
        <v-icon icon="mdi-calendar-blank" size="x-large" />
        <p class="font-weight-bold text-body-1 mt-3">No current events :(</p>
        <v-btn
          v-if="user?.teamAdmin"
          size="x-large"
          class="bg-primaryRed text-primaryWhite mt-3"
          @click="isAddingEvent = true"
          >ADD EVENT
        </v-btn>
      </div>
    </div>
  </v-container>
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
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

const eventStore = useEventStore()
const { user } = storeToRefs(useUserStore())
const isLoading = ref(true)

onMounted(async () => {
  try {
    await eventStore.getEvents()
  } catch (e) {
    console.log(e)
  }
  isLoading.value = false
})

const searchQuery = ref<string | undefined>('') // pressing the clear button sets the text field to undefined
const filteredEventsList = computed<Event[]>(() =>
  eventStore.events.filter(
    (e) =>
      !searchQuery.value ||
      (e.name + e.description).toLowerCase().includes(searchQuery.value.toLowerCase())
  )
)
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
/* #cards-container > .v-card:nth-child(odd) {
  background-color: #f4f4f4;
} */

.v-field__input {
  padding-top: 19px;
  padding-bottom: 0px;
  margin-top: -19px;
}
</style>
