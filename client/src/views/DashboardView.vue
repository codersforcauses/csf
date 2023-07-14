<<<<<<< HEAD
 <template>
  <div class="about">
  <v-card
    class="mx-auto"
    width="300"
  >
    <v-list v-model:opened="open">
      <v-list-item prepend-icon="mdi-home" title="Home"></v-list-item>

      <v-list-group value="Users">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-account-circle"
            title="Sub-teams"
          ></v-list-item>
        </template>

        <v-list-group value="Admin">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="Sub-teams1"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            :title="title"
            :prepend-icon="icon"
            :value="title"
          ></v-list-item>
        </v-list-group>

             <v-list-group value="Admin">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="Sub-teams2"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            :title="title"
            :prepend-icon="icon"
            :value="title"
          ></v-list-item>
        </v-list-group>

  
      </v-list-group>
    </v-list>
  </v-card>
  </div>
</template>


<script>
  export default {
    data: () => ({
      open: ['Users'],
      admins: [
        ['Management', 'mdi-account-multiple-outline'],
        ['Settings', 'mdi-cog-outline'],
      ],
      cruds: [
        ['Create', 'mdi-plus-outline'],
        ['Read', 'mdi-file-outline'],
        ['Update', 'mdi-update'],
        ['Delete', 'mdi-delete'],
      ],
    }),
  }
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
=======
<template>
  <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center" justify="center">
    <h1>Welcome back, {{ tempUserFirstName }}!</h1>
  </v-row>
  <v-divider />
  <v-row class="ma-0 pl-4 pr-4 pb-0 pt-0" align="center">
    <v-col>
      <v-card variant="flat" class="pb-1">
        <v-container class="pa-0" fluid>
          <v-row class="ma-0">
            <v-col cols="auto" class="pl-0 pr-0">
              <v-icon icon="mdi-run-fast" size="52" />
            </v-col>
            <v-col>
              <v-chip color="green" class="rounded text-h5">{{ tempUserMileage }} KM</v-chip>
              <v-card-subtitle>TOTAL</v-card-subtitle>
            </v-col>
            <v-spacer />
            <v-col cols="auto">
              <v-btn
                variant="elevated"
                elevated="2"
                :ripple="true"
                icon="mdi-plus"
                color="primaryRed"
                @click="dialog = true"
              />
              <MileageModal v-model="dialog" />
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
  <v-divider />
  <v-row class="ma-0 px-4 pt-0 pb-0" align="center">
    <v-col>
      <h2>Daily KMs</h2>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MileageModal from '../components/MileageModal.vue'

const tempUserFirstName = ref('John')
const tempUserMileage = ref(100)
const dialog = ref(false)
</script>

<style scoped></style>
>>>>>>> main
