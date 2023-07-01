<template>
<v-dialog fullscreen>
    <v-card color="#ECECEC">
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-icon class="me-1" icon="mdi-close" @click="closeModal"></v-icon>
      </v-card-actions>
      <v-card-title class="justify-center text-h4">Create Event</v-card-title>
      <v-text-field hide-details bg-color="white" label="Event Name"></v-text-field>
      <v-text-field hide-details bg-color="white" label="Start Date" type="date"></v-text-field>
      <v-text-field hide-details bg-color="white" label="End Date" type="date"></v-text-field>
      <v-textarea hide-details bg-color="white" label="Description"></v-textarea>
      <v-card-actions class="justify-center">
        <v-btn class="bg-primaryRed" @click="addEvent">CREATE</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
    interface Props {
        display: boolean
        type: "Create" | "Edit"
    }
    defineProps<Props>()
    const emit = defineEmits(['close'])

    function addEvent() {
        closeModal()
    }

    function closeModal() {
        emit('close')
    }
</script>