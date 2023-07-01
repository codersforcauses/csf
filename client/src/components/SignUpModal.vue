<template>
  <v-row justify="center" items="center" class="width">
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="912px">
      <v-card style="height: 100%;">
        <div v-if="firstPage">
          <form style="background-color:#ECECEC;">
            <v-container class="pa-0">
              <v-img src="/images/Footer-min.jpeg" width="100%" height="10" cover></v-img>
            </v-container>
            <v-row justify="end">
              <v-col cols="auto">
                <v-btn variant="text" @click="closeModal"> <v-icon icon="mdi-close" size="32px"></v-icon></v-btn>
              </v-col>
            </v-row>
            <v-card-title class="d-flex justify-center">
              <v-card flat color="#ECECEC">
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
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.username" label="Username"
                      required></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.firstName" label="First name"
                      required></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.lastName"
                      label="Last name"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6">
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.email" label="Email"
                      required></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.password" label="Password"
                      type="password" required></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field bg-color="#FFFFFF" :rules="[required]" v-model="state.confirmPassword"
                      label="Confirm Password" type="password" required></v-text-field>
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
                    <!-- todo add in routing to login modal when its ready -->
                    <v-btn variant="text" color="secondaryBlue" style="font-size: 12px;">Already Have an
                      account?</v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-actions>
          </form>
        </div>
        <div v-if="!firstPage">
          <form style="background-color:#ECECEC; bottom: auto;" @submit.prevent="">
            <v-container class="pa-0">
              <v-img src="/images/Footer-min.jpeg" width="auto" height="10" cover></v-img>
            </v-container>
            <v-row justify="end">
              <v-col cols="auto">
                <v-btn variant="text" @click="closeModal">
                  <v-icon icon="mdi-close" size="32px"></v-icon></v-btn>
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
                  <v-row>
                    <v-col cols="12">
                      <p>Select an Avatar</p>
                    </v-col>
                    <v-row>
                      <v-col v-for="avatar in avatarPaths" :key="avatar.url" cols="4">
                        <div style="padding-top: 5px; padding-bottom: 5px;" class="text-center">
                          <v-avatar size="80" @click="selectAvatar(avatar.url)"
                            :class="{ 'avatar-selected': avatar.isSelected === true }">
                            <v-img :src="avatar.url" :alt="avatar.alt"></v-img>
                          </v-avatar>
                        </div>
                      </v-col>
                    </v-row>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <p style="padding-top: 5px;">Select main method of travel</p>
                    </v-col>
                    <v-container class="d-flex  justify-space-evenly">
                      <div v-for="method in  travelMethod " :key="method.logo" class="text-center">
                        <v-avatar size="52px" variant="text"
                          :class="{ 'mode-selected': method.isSelected === true }"><v-icon
                            :color="method.isSelected ? 'white' : ''" size="44px" :icon="method.logo"
                            @click="() => { selectMode(method.mode) }"></v-icon>
                        </v-avatar>
                        <p>{{ method.mode }}</p>
                      </div>
                    </v-container>
                  </v-row>
                  <v-container fluid fill-height class="my-4">
                    <v-row no-gutters>
                      <v-col cols="12">
                        <v-checkbox density="default" v-model="state.teamSignup"
                          label="I am signing up on behalf of a class"></v-checkbox>
                      </v-col>
                      <v-col cols="12">
                        <v-checkbox density="default" v-model="state.hasConsent"
                          label="I give consent for my data to be used by CSF"></v-checkbox>
                        <p class=" text-caption">For more information please view <span
                            style="text-decoration: underline; color: blue;"><a href="https://www.google.com">our
                              privacy
                              statement</a></span></p>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-container>
                <v-row align="center" justify="center">
                  <v-col cols="auto">
                    <v-btn variant="text" class="mx-2" @click="firstPage = !firstPage">BACK</v-btn>
                    <v-btn variant="flat" class="mx-2" rounded="lg" color="primaryRed" @click="submit">CREATE
                      ACCOUNT</v-btn>
                  </v-col>
                </v-row>
                <v-row align="center" justify="center">
                  <v-col cols="auto">
                    <!-- todo add in routing to login modal when its ready -->
                    <v-btn variant="text" color="secondaryBlue" style="font-size: 12px;">Already Have an
                      account?</v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-actions>
          </form>
        </div>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script setup lang="ts">
import avatar1 from "../assets/Avatars/avatar1.jpg";
import avatar2 from "../assets/Avatars/avatar2.jpg";
import avatar3 from "../assets/Avatars/avatar3.jpg";
import avatar4 from "../assets/Avatars/avatar4.jpg";
import avatar5 from "../assets/Avatars/avatar5.jpg";
import avatar6 from "../assets/Avatars/avatar6.jpg";
import { ref, reactive } from 'vue'
import { useDisplay } from 'vuetify'
import { type Signup } from '../types/signup'

defineProps(['dialogModal'])
const emit = defineEmits(["modalTrigger"])

const closeModal = () => {
  emit("modalTrigger", false);
}

const { mobile } = useDisplay()
const firstPage = ref<boolean>(true);
const dialog = ref(true)
const avatarPaths = ref([{ url: avatar1, alt: "avatar1", isSelected: true }, { url: avatar2, alt: "avatar2", isSelected: false }, { url: avatar3, alt: "avatar3", isSelected: false }, { url: avatar4, alt: "avatar4", isSelected: false }, { url: avatar5, alt: "avatar5", isSelected: false }, { url: avatar6, alt: "avatar6", isSelected: false }]);
const travelMethod = ref([{ logo: "mdi-run-fast", mode: "RUNNING", isSelected: true }, { logo: "mdi-wheelchair-accessibility", mode: "WHEELING", isSelected: false }, { logo: "mdi-walk", mode: "WALKING", isSelected: false }]);

const state = reactive<Signup>({
  username: "",
  firstName: "",
  lastName: "",
  email: "",
  password: "",
  confirmPassword: "",
  teamSignup: false,
  hasConsent: false,
  avatar: "",
  method: ""
})

const submit = async () => {
  // need this here as default values sorta mess stuff up but it works
  const avatar = avatarPaths.value.filter((avatar) => avatar.isSelected === true)
  const method = travelMethod.value.filter((method) => method.isSelected === true)
  state.method = method[0].mode;
  state.avatar = avatar[0].url;
  console.log(state)
}

const selectAvatar = (url: string) => {
  avatarPaths.value.forEach((avatar) => {
    if (avatar.url === url)
      avatar.isSelected = !avatar.isSelected;
    if (avatar.url !== url)
      avatar.isSelected = false;
  })
  state.avatar = url;
}

const selectMode = (mode: string) => {
  travelMethod.value.forEach((method) => {
    if (method.mode === mode)
      method.isSelected = !method.isSelected;
    if (method.mode !== mode)
      method.isSelected = false;
  })
  state.method = mode;
}

const required = (v: string) => {
  return !!v || 'Field is required'
};
</script>

<style scoped>
.avatar-selected {
  border: 6px solid #345E9E !important;
}

.mode-selected {
  background-color: #345E9E !important;
}
</style>
                