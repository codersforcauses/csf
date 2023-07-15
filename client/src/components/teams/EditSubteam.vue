<template>
  <v-row>
      <div>Subteam1</div>
      <div>60KM</div>
      <div>Members</div>
      <v-select :items="['1', '2', '3']" label="Select" outlined dense>
      </v-select>
      <v-list>
          <v-list-item-group color="primary">
              <v-list-item v-for="(subteam, index) in subteams" :key="index">
                  <v-list-item-content> {{ subteam.teamName }}</v-list-item-content>
                  <v-list-item-content> {{ subteam.currentStatus }}</v-list-item-content>
                  <v-list-item-content> {{ subteam.members }}</v-list-item-content>
                  <v-list-item-content> {{ subteam.teamId }}</v-list-item-content>
              </v-list-item>
          </v-list-item-group>
      </v-list>
  </v-row>
</template>

<script setup lang="ts">
import { ref, reactive, toRefs, onBeforeMount, onMounted, watchEffect, computed } from 'vue';
defineProps(['isSubTeamsVisible'])
const data = reactive({


})
defineExpose({
  ...toRefs(data)
})

</script>
<style scoped  >
/* .v-list-item {
  padding: 4px 10px !important;
} */
</style>