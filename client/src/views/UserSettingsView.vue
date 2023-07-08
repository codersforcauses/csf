<template>
  <v-btn class="bg-primaryRed ma-4" @click="showChangePasswordModal = true">Change Password </v-btn>
  <ChangePasswordModal v-if="showChangePasswordModal" v-model="showChangePasswordModal" @close="showChangePasswordModal = false" @success="passwordChanged"/>
</template>

<script setup lang="ts">
import PopupDialog from '@/components/PopupDialog.vue';
import ChangePasswordModal from '../components/ChangePasswordModal.vue'
import { ref } from 'vue'

const showChangePasswordModal = ref(false)
const showSuccessDialog = ref(false)

function passwordChanged() {
  showChangePasswordModal.value = false
  showSuccessDialog.value = true
}

</script>
