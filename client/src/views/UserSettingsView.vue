<template>
  <v-btn class="bg-primaryRed ma-4" @click="showChangePasswordModal = true">Change Password </v-btn>
  <ChangePasswordModal v-model="showChangePasswordModal" @close="showChangePasswordModal = false"/>
</template>

<script setup lang="ts">
import ChangePasswordModal from '../components/ChangePasswordModal.vue'
import { ref } from 'vue'

const showChangePasswordModal = ref(false)

</script>
