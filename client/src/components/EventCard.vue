<template>
  <v-card class="mx-3 elevation-0" :class="backgroundColour">
    <v-card-title>
      <span class="font-weight-bold">{{ event.name }}</span>
      <v-spacer />
      <v-icon
        v-if="isTeamAdmin && !event.isPublic"
        icon="mdi-pencil"
        @click="openModal"
        size="24"
        class="mr-2 mt-1"
      />
      <v-chip
        variant="outlined"
        :class="event.isPublic ? 'text-secondaryBlue' : 'text-secondaryGreen'"
      >
        {{ event.isPublic ? 'Official' : 'Private' }}
      </v-chip>
      <v-chip v-if="event.isArchived"> Archived </v-chip>
    </v-card-title>
    <v-card-subtitle class="text-primaryRed font-italic"
      >{{ event.startDate }} - {{ event.endDate }}</v-card-subtitle
    >
    <v-card-text>{{ event.description }}</v-card-text>
  </v-card>
  <v-divider class="mx-4" />
</template>

<script setup lang="ts">
import { type Event } from '../types/event'
const props = defineProps<{ event: Event; isTeamAdmin: boolean; backgroundColour: string }>()
const emit = defineEmits(['edit'])

function openModal() {
  emit('edit', props.event.eventId)
}
</script>

<style>
.v-card-title {
  display: flex;
}
</style>
