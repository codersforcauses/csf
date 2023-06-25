<template>
    <section>
        <v-row justify="center" items="center" class="width">
            <v-dialog v-model="dialog" :fullscreen="mobile" max-width="912px">
                <template v-slot:activator="{ props }">
                    <v-btn v-bind="props">Signup</v-btn>
                </template>
                <v-card>
                    <form @submit.prevent="submit()">
                        <v-card-title>
                            <span class="text-h5">Signup</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.firstName" label="First name" required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.lastName" label="Last name"
                                            hint="example of helper text only on focus"></v-text-field>
                                    </v-col>

                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.email" label="Email*" required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.confirmEmail" label="Confirm Email*"
                                            required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.password" label="Password*" type="password"
                                            required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6">
                                        <v-text-field v-model="state.confirmPassword" label="Confirm Password*"
                                            type="password" required></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6">
                                        <v-select v-model="state.avatar"
                                            :items="['avatar1', 'avatar2', 'avatar3', 'avatar4']" label="Avatar"
                                            required></v-select>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-checkbox v-model="state.teamSignup"
                                            label="If signing up on behalf of a class, please tick"></v-checkbox>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-checkbox v-model="state.hasConsent"
                                            label="Does Community Spirit Foundation have permission to use your data?"></v-checkbox>
                                    </v-col>
                                </v-row>
                                <large>*indicates required field</large>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                                Close
                            </v-btn>
                            <v-btn color="blue-darken-1" variant="text" @click="dialog = false; submit();">
                                Submit
                            </v-btn>
                        </v-card-actions>
                    </form>
                </v-card>
            </v-dialog>
        </v-row>
    </section>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useDisplay } from "vuetify"
import signup from "../types/signup";

const { mobile } = useDisplay();



const emit = defineEmits(['submit']);

const dialog = ref(false)


const state: signup = reactive({});

const submit = () => {
    console.log(state);
}

</script>
