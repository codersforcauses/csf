
<template>
  <v-toolbar>
    <v-text-field prepend-inner-icon="mdi-magnify" hide-details label="Search Events" v-model="searchQuery"/>
    <v-btn v-if="tempIsTeamAdmin" icon="mdi-plus" size="small" id="add-event-btn"></v-btn>
  </v-toolbar>
  
  <Event v-for="event in filteredEventsList" :name="event.name" :startDate="event.startDate" :endDate="event.endDate" :description="event.description" :canEdit="tempIsTeamAdmin && event.isPrivate" :isPrivate="event.isPrivate"/>
</template>

<script setup lang="ts">
  import Event from '../components/Event.vue'
  import { ref, computed } from 'vue'
  const temporaryEventsList = ref([
    {name: "Run Very Far", startDate: "17 Nov", endDate: "23 Nov", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", isPrivate: false},
    {name: "Run Even Further", startDate: "25 Nov", endDate: "2 Dec", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat", isPrivate: true},
    {name: "Walk", startDate: "6 Dec", endDate: "6 Dec", description: "Designers use Lorem Ipsum as a dummy text, something to cover the fact that content is missing from the wireframe. “Lorem Ipsum” is followed by more Latin text, making it easy for users or other designers to ignore it and imagine something more familiar or relevant in its place.", isPrivate: true},
  ])
  const searchQuery = ref("")
  const filteredEventsList = computed(() => {
    let query = searchQuery.value.toLowerCase()
    return temporaryEventsList.value.filter( e => e.name.toLowerCase().includes(query) || e.description.toLowerCase().includes(searchQuery.value))
  })
  const tempIsTeamAdmin = ref(true)

</script> 

<style>
  #add-event-btn {
    background-color: rgb(var(--v-theme-primaryRed));
    color: rgb(var(--v-theme-primaryWhite));
    font-size: 20px;
    margin-right: 20px;
  }
  .v-toolbar {
    background-color: rgb(var(--v-theme-primaryWhite));
  }
  .v-text-field {
    margin: 20px;
  }
</style>
