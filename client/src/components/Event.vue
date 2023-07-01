<template>
  <v-card class="mx-3">
    <v-card-title>
      <span class="font-weight-bold">{{ name }}</span>
      <v-icon v-if="canEdit" icon="mdi-pencil" @click="openModal"></v-icon>
      <v-spacer></v-spacer>
      <v-chip
        variant="outlined"
        :class="{ 'text-secondaryGreen': isPrivate, 'text-secondaryBlue': !isPrivate }"
        >{{ isPrivate ? 'Private' : 'Official' }}</v-chip
      >
    </v-card-title>
    <v-card-subtitle class="text-primaryRed font-italic">{{ startDate }} - {{ endDate }}</v-card-subtitle>
    <v-card-text>{{ description }}</v-card-text>
  </v-card>
</template>

<script setup lang="ts">
interface Props {
  id: number
  name: string
  startDate: string
  endDate: string
  description: string
  canEdit: boolean
  isPrivate: boolean
}
const props = defineProps<Props>()
const emit = defineEmits(['edit'])

function openModal() {
  emit('edit', props.id)
}
</script>

<style>
.v-card-title {
  display: flex;
}
</style>
