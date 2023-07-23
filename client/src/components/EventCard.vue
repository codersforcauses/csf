<template>
  <v-card class="mx-3 elevation-0" :class="backgroundColour">
    <v-card-title style="word-break: break-word; overflow-wrap: break-word; white-space: normal">
      <v-row no-gutters>
        <span class="font-weight-bold">{{ event.name }}</span>
        <v-icon
          v-if="user?.teamAdmin && !event.isPublic"
          icon="mdi-pencil"
          @click="openModal"
          size="24"
          class="mr-2 mt-1"
        />
        <v-spacer />
        <v-chip
          variant="outlined"
          :class="event.isPublic ? 'text-secondaryBlue' : 'text-secondaryGreen'"
        >
          {{ event.isPublic ? 'Official' : 'Private' }}
        </v-chip>
      </v-row>
    </v-card-title>
    <v-card-subtitle class="text-primaryRed font-italic"
      >{{ event.startDate }} - {{ event.endDate }}</v-card-subtitle
    >
    <v-card-text>{{ event.description }}</v-card-text>
  </v-card>
  <v-divider class="mx-4" />
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import { type Event } from '../types/event'
import { storeToRefs } from 'pinia'
const props = defineProps<{ event: Event; backgroundColour: string }>()
const emit = defineEmits(['edit'])

const { user } = storeToRefs(useUserStore())

function openModal() {
  emit('edit', props.event.eventId)
}
</script>

<style>
.v-card-title {
  display: flex;
}
</style>
