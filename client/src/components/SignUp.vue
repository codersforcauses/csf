<template>
  <section>
    <v-row justify="center" items="center" class="width">
      <v-dialog v-model="dialog" :fullscreen="mobile" max-width="912px">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props">Signup</v-btn>
        </template>
        <v-card>
          <div v-if="firstPage">
            <form style="background-color:#ECECEC; bottom: auto;" @submit.prevent="">
              <v-divider class="border-opacity-100" :thickness="12" color="primaryRed"></v-divider>
              <v-row justify="end">
                <v-col cols="auto">
                  <v-btn variant="text" @click="() => { dialog = false; }"><svg-icon type="mdi"
                      :path="path"></svg-icon></v-btn>
                </v-col>
              </v-row>
              <v-card-title class="d-flex justify-center">
                <v-card class="" flat color="#ECECEC">
                  <v-card-item>
                    <v-card-title class="text-center text-h4 pb-2">Register</v-card-title>
                    <v-card-subtitle class="text-center text-subtitle-1
">Create an account</v-card-subtitle>
                  </v-card-item>
                </v-card>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.username" label="Username" required></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.firstName" label="First name"
                        required></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.lastName" label="Last name"></v-text-field>
                    </v-col>

                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.email" label="Email" required></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.password" label="Password" type="password"
                        required></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field :rules="[required]" v-model="state.confirmPassword" label="Confirm Password"
                        type="password" required></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-container>
                  <v-row align="center" justify="center">
                    <v-col cols="auto">
                      <v-btn variant="flat" rounded="lg" color="primaryRed"
                        @click="() => { firstPage = !firstPage }">NEXT</v-btn>
                    </v-col>
                  </v-row>
                  <v-row align="center" justify="center">
                    <v-col cols="auto">
                      <v-btn variant="text">Already Have an account?</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-actions>
            </form>
          </div>
          <div v-if="!firstPage">
            <form style="background-color:#ECECEC; bottom: auto;" @submit.prevent="">
              <v-divider class="border-opacity-100" :thickness="12" color="primaryRed"></v-divider>
              <v-row justify="end">
                <v-col cols="auto">
                  <v-btn variant="text" @click="() => { dialog = false; }"><svg-icon type="mdi"
                      :path="path"></svg-icon></v-btn>
                </v-col>
              </v-row>
              <v-card-title class="d-flex justify-center">
                <v-card class="" flat color="#ECECEC">
                  <v-card-item>
                    <v-card-title class="text-center text-h4 pb-2">Register</v-card-title>
                    <v-card-subtitle class="text-center text-subtitle-1
">Create an account</v-card-subtitle>
                  </v-card-item>
                </v-card>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <div v-for="image in avatarPaths" :key="image.url">
                        <p>{{ Object.keys(image) }}</p>
                        <img :src="image.url" :alt="image.alt">
                      </div>
                    </v-col>
                    <v-col cols="12">
                      <v-checkbox :rules="[required]" v-model="state.teamSignup"
                        label="If signing up on behalf of a class, please tick"></v-checkbox>
                    </v-col>
                    <v-col cols="12">
                      <v-checkbox :rules="[required]" v-model="state.hasConsent"
                        label="Does Community Spirit Foundation have permission to use your data?"></v-checkbox>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-container>
                  <v-row align="center" justify="center">
                    <v-col cols="auto">
                      <v-btn variant="flat" rounded="lg" color="primaryRed" @click="submit">CREATE ACCOUNT</v-btn>
                    </v-col>
                  </v-row>
                  <v-row align="center" justify="center">
                    <v-col cols="auto">
                      <v-btn variant="text">Already Have an account?</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-actions>
            </form>
          </div>
        </v-card>
      </v-dialog>
    </v-row>
  </section>
</template>

<script setup lang="ts">
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiClose } from '@mdi/js';
import { ref, reactive, onMounted } from 'vue'
import { useDisplay } from 'vuetify'
import signup from '../types/signup'

const { mobile } = useDisplay()
const path = mdiClose;
const firstPage = ref(true);
const dialog = ref(false)
const avatarPaths = [{url: "../assets/Avatars/avatar1.jpg", alt: "avatar1"}, {url: "../assets/Avatars/avatar2.jpg", alt: "avatar2"},{url: "../assets/Avatars/avatar3.jpg", alt: "avatar3"}, {url: "../assets/Avatars/avatar4.jpg", alt: "avatar4"}, {url: "../assets/Avatars/avatar5.jpg", alt: "avatar5"}, {url: "../assets/Avatars/avatar6.jpg", alt: "avatar6"}];

onMounted(async () => {
  try {
    // await getPhotos();
  } catch (error) {
    console.log(error);
  }
  // console.log(avatarImages);

})

const state: signup = reactive({})

const submit = () => {
  console.log(state)
}

const required = (v: string) => {
  return !!v || 'Field is required'
};
</script>

<!-- stuff to move  -->
<!-- <v-btn color="blue-darken-1" variant="text" @click="dialog = false"> Close </v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="() => {
                  ; (dialog = false), submit()
                }
                  ">
                  Submit
                </v-btn> -->
                