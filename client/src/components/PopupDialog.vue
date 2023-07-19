<script setup lang="ts">
import { computed, ref } from 'vue'
// import { useDisplay } from 'vuetify'

const isFullscreen = ref(false)
const emit = defineEmits(['update:modelValue', 'handleSubmit'])
const props = defineProps(['modelValue', 'title', 'text', 'submitText'])

const value = computed({
  get() {
    return props.modelValue
  },
  set(value) {
    emit('update:modelValue', value)
  }
})
</script>

<template>
  <v-dialog v-model="value" :fullscreen="isFullscreen" max-width="500px">
    <v-card class="d-flex flex-column">
      <div style="height: 8px">
        <v-img src="/images/Footer-min.jpeg" width="100%" alt="red background" cover />
      </div>
      <v-card-item>
        <v-card-title>{{ title }}</v-card-title>
      </v-card-item>
      <v-card-text>{{ text }}</v-card-text>
      <v-spacer></v-spacer>
      <v-card-actions class="d-flex justify-end bg-backgroundGrey">
        <v-btn @click="$emit('update:modelValue', !modelValue)">Cancel</v-btn>
        <v-btn
          variant="elevated"
          color="primaryRed"
          @click="
            () => {
              $emit('handleSubmit')
              $emit('update:modelValue', !modelValue)
            }
          "
          >{{ submitText }}</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
