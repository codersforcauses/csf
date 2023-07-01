
<template>
  <v-toolbar class="bg-primaryWhite">
    <v-text-field prepend-inner-icon="mdi-magnify" hide-details label="Search Events" clearable v-model="searchQuery"/>
    <v-btn v-if="tempIsTeamAdmin" icon="mdi-plus" size="small" id="add-event-btn" class="bg-primaryRed text-primaryWhite" @click="addingEvent = true"></v-btn>
  </v-toolbar>
  <Event v-for="event in filteredEventsList" :name="event.name" :startDate="event.startDate" :endDate="event.endDate" :description="event.description" :canEdit="tempIsTeamAdmin && event.isPrivate" :isPrivate="event.isPrivate"/>
  <v-dialog v-model="addingEvent" fullscreen>
      <v-card color="#ECECEC">
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-icon class="me-1" icon="mdi-close" @click="addingEvent = false"></v-icon>
        </v-card-actions>
        <v-card-title class="justify-center">Add Event</v-card-title>
        <v-text-field hide-details bg-color="white" label="Event Name"></v-text-field>
        <v-text-field hide-details bg-color="white" label="Start Date" type="date"></v-text-field>
        <v-text-field hide-details bg-color="white" label="End Date" type="date"></v-text-field>
        <v-textarea hide-details bg-color="white" label="Description"></v-textarea>
      </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
  import Event from '../components/Event.vue'
  import { ref, computed } from 'vue'

  interface Event {
    name: string
    startDate: string
    endDate: string
    description: string
    isPrivate: boolean
  }

  const temporaryEventsList = ref<Event[]>([
    {name: "Run Very Far", startDate: "17 Nov", endDate: "23 Nov", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", isPrivate: false},
    {name: "Run Even Further", startDate: "25 Nov", endDate: "2 Dec", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", isPrivate: true},
    {name: "Walk", startDate: "6 Dec", endDate: "6 Dec", description: "Designers use Lorem Ipsum as a dummy text, something to cover the fact that content is missing from the wireframe. “Lorem Ipsum” is followed by more Latin text, making it easy for users or other designers to ignore it and imagine something more familiar or relevant in its place.", isPrivate: true},
    {name: "Walk again", startDate: "7 Dec", endDate: "7 Dec", description: "walk again!", isPrivate: false},
  ])
  const searchQuery = ref<string>("")
  const filteredEventsList = computed<Event[]>(() => {
    let query: string = searchQuery.value ? searchQuery.value.toLowerCase() : ""
    return temporaryEventsList.value.filter( e => e.name.toLowerCase().includes(query) || e.description.toLowerCase().includes(searchQuery.value))
  })
  const tempIsTeamAdmin = ref<boolean>(true)
  const addingEvent = ref<boolean>(false)
</script> 

<style>
  #add-event-btn {
    font-size: 20px;
    margin-right: 20px;
  }
  .v-text-field {
    margin: 20px;
  }
</style>
