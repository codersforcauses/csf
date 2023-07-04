<script setup lang="ts">
import { ref } from 'vue'
import PopupDialog from '../components/PopupDialog.vue'

// should this be a single object or multiple refs
const display = ref(false)
const title = ref('Title')
const text = ref('text paragraph writing words')
const submitText = ref('Create')

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
</template>
