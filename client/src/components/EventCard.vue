<template>
  <v-card class="mx-3">
    <v-card-title>
      <span class="font-weight-bold">{{ event.name }}</span>
      <v-icon v-if="isTeamAdmin && !event.isPublic" icon="mdi-pencil" @click="openModal"></v-icon>
      <v-spacer></v-spacer>
      <v-chip
        variant="outlined"
        :class="{ 'text-secondaryGreen': !event.isPublic, 'text-secondaryBlue': event.isPublic }"
        >{{ !event.isPublic ? 'Private' : 'Official' }}</v-chip
      >
    </v-card-title>
    <v-card-subtitle class="text-primaryRed font-italic"
      >{{ event.startDate }} - {{ event.endDate }}</v-card-subtitle
    >
    <v-card-text>{{ event.description }}</v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import {type Event} from '../types/event'
const props = defineProps<{ event: Event; isTeamAdmin: boolean }>()
const emit = defineEmits(['edit'])

function openModal() {
  emit('edit', props.event.id)
}
</script>

<style>
.v-card-title {
  display: flex;
}
</style>
