<script setup lang="ts">
import { ref } from 'vue'
import PopupDialog from '../components/PopupDialog.vue'

// should this be a single object or multiple refs
const display = ref(false)
const title = ref('Title')
const text = ref('text paragraph writing words')
const submit = ref('Create')

const handleSubmit = () => {
  console.log('Submit')
}
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/login">Login</RouterLink>
    <RouterLink to="/signup">signup</RouterLink>
  </nav>
  <v-btn @click="display = true">
    <PopupDialog
      v-model="display"
      :title="title"
      :text="text"
      :submit="submit"
      @handle-submit="handleSubmit"
    />
    Popup
  </v-btn>
</template>
