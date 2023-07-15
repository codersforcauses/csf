<template>
  <v-alert :color="`${props.color}`" :icon="`${props.icon}`" :text="`${props.message}`" closable>
  </v-alert>
</template>
<script setup lang="ts">
const props = defineProps<{
  color: string
  icon: string
  message: string
}>()
</script>
