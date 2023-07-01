<script setup lang="ts">
import { computed } from 'vue'
import { useDisplay } from 'vuetify'

const emit = defineEmits(['update:modelValue', 'handleSubmit'])
const props = defineProps(['modelValue', 'display', 'title', 'text', 'submit'])

const value = computed({
  get() {
    return props.modelValue
  },
  set(value) {
    emit('update:modelValue', value)
  }
})

const { mobile } = useDisplay()
</script>

<template>
  <v-dialog v-model="value" :fullscreen="mobile" max-width="912px">
    <div class="title">{{ title }}</div>
    <div class="text">{{ text }}</div>
    <div class="footer">
      <v-btn class="modal-default-button" @click="$emit('update:modelValue', !modelValue)"
        >cancel</v-btn
      >
      <v-btn
        class="modal-default-button"
        @click="
          () => {
            $emit('handleSubmit')
            $emit('update:modelValue', !modelValue)
          }
        "
      >
        {{ submit }}
      </v-btn>
    </div>
  </v-dialog>
</template>

<style scoped></style>
