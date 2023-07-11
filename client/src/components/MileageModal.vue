<template>
    <v-dialog v-model="value" :fullscreen="isFullscreen" width="500px">
        <v-card height="700px" class="bg-backgroundGrey">
            <div style="height:10px">
                <v-img src="/images/Footer-min.jpeg" width="100%" cover />
            </div>
            <v-spacer/>
            <v-form v-model="form">
                <v-container class="px-8">
                    <v-row align="center">
                        <v-col>
                            <v-card-title class="mx-auto text-h5 justify-center">Add Mileage</v-card-title>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-card-text>
                            <v-row>
                                <v-col>
                                    <v-text-field
                                        type="date"
                                        label="Date"
                                        v-model="date"
                                        bg-color="white"
                                        :rules="[required]"
                                    />
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <div v-if="tempIconType === 'running'" class="ma-0 pa-0" id="runner">
                                        <v-slider
                                            v-model="distance"
                                            color="green"
                                            :thumb-size="40"
                                            elevation="0"
                                            :step="1"
                                            min="1"
                                            max="100"
                                        />
                                    </div>
                                    <div v-if="tempIconType === 'walking'" id="walker" class="ma-0 pa-0">
                                        <v-slider
                                            v-model="distance"
                                            color="green"
                                            :thumb-size="40"
                                            elevation="0"
                                            :step="1"
                                            min="1"
                                            max="100"
                                        />
                                    </div>
                                    <div v-if="tempIconType === 'wheeling'" id="wheeler" class="ma-0 pa-0">
                                        <v-slider
                                            v-model="distance"
                                            color="green"
                                            :thumb-size="40"
                                            elevation="0"
                                            :step="1"
                                            min="1"
                                            max="100"
                                        />
                                    </div>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col align="center">
                                    <v-chip class="px-6 text-h5 rounded"
                                        color="green"
                                    >{{ distance }}</v-chip>
                                    <p class="text-subtitle-2">KILOMETERS</p>
                                </v-col>
                            </v-row>
                        </v-card-text>
                    </v-row>
                </v-container>
                <v-card-actions class="d-flex justify-center">
                    <v-btn @click="$emit('update:modelValue', !modelValue)">CANCEL</v-btn>
                    <v-btn @click="handleSubmit" :disabled="!form" color="primaryRed" variant="elevated">ADD</v-btn>
                </v-card-actions>
            </v-form>
            <v-spacer/>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
    import { computed } from 'vue'
    import { ref, watchEffect } from 'vue'
    
    const isFullscreen = ref(false)
    const props = defineProps(['modelValue'])
    const emit = defineEmits(['update:modelValue', 'handleSubmit'])
    const distance = ref(1)
    const date = ref('')
    const form = ref(false)
    const required = (v: string) => {
        return !!v || 'Field is required'
    }

    // The icon on the slider changes depending on this variable. Current temp options are "running" | "walking" | "wheeling"
    const tempIconType: string = "running"

    const value = computed({
        get() {
            return props.modelValue
        },
        set(value) {
            emit('update:modelValue', value)
        }
    })

    const handleSubmit = () => {
        console.log(date.value)
        console.log(distance.value)
        emit('update:modelValue', false)
    }

    // Copied from SignUpModal 
    watchEffect(async () => {
        const updateFullscreen = async () => {
            isFullscreen.value = window.innerWidth <= 500 // Adjust the breakpoint as needed
        }

        // Initial update
        await updateFullscreen()

        // Add window resize event listener
        window.addEventListener('resize', updateFullscreen)

        // Cleanup: Remove window resize event listener
        return () => {
            window.removeEventListener('resize', updateFullscreen)
        }
    })
</script>

<style scoped>
    #runner :deep(.v-slider-thumb__surface) {
        border-radius: 0% !important; 
        background-color: transparent !important;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>run</title><path d="M13.5,5.5C14.59,5.5 15.5,4.58 15.5,3.5C15.5,2.38 14.59,1.5 13.5,1.5C12.39,1.5 11.5,2.38 11.5,3.5C11.5,4.58 12.39,5.5 13.5,5.5M9.89,19.38L10.89,15L13,17V23H15V15.5L12.89,13.5L13.5,10.5C14.79,12 16.79,13 19,13V11C17.09,11 15.5,10 14.69,8.58L13.69,7C13.29,6.38 12.69,6 12,6C11.69,6 11.5,6.08 11.19,6.08L6,8.28V13H8V9.58L9.79,8.88L8.19,17L3.29,16L2.89,18L9.89,19.38Z" /></svg>');
        background-size: cover;
    }

    #walker :deep(.v-slider-thumb__surface) {
        border-radius: 0% !important; 
        background-color: transparent !important;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>walk</title><path d="M14.12,10H19V8.2H15.38L13.38,4.87C13.08,4.37 12.54,4.03 11.92,4.03C11.74,4.03 11.58,4.06 11.42,4.11L6,5.8V11H7.8V7.33L9.91,6.67L6,22H7.8L10.67,13.89L13,17V22H14.8V15.59L12.31,11.05L13.04,8.18M14,3.8C15,3.8 15.8,3 15.8,2C15.8,1 15,0.2 14,0.2C13,0.2 12.2,1 12.2,2C12.2,3 13,3.8 14,3.8Z" /></svg>');
        background-size: cover;
    }

    #wheeler :deep(.v-slider-thumb__surface) {
        border-radius: 0% !important; 
        background-color: transparent !important;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>wheelchair-accessibility</title><path d="M18.4,11.2L14.3,11.4L16.6,8.8C16.8,8.5 16.9,8 16.8,7.5C16.7,7.2 16.6,6.9 16.3,6.7L10.9,3.5C10.5,3.2 9.9,3.3 9.5,3.6L6.8,6.1C6.3,6.6 6.2,7.3 6.7,7.8C7.1,8.3 7.9,8.3 8.4,7.9L10.4,6.1L12.3,7.2L8.1,11.5C8,11.6 8,11.7 7.9,11.7C7.4,11.9 6.9,12.1 6.5,12.4L8,13.9C8.5,13.7 9,13.5 9.5,13.5C11.4,13.5 13,15.1 13,17C13,17.6 12.9,18.1 12.6,18.5L14.1,20C14.7,19.1 15,18.1 15,17C15,15.8 14.6,14.6 13.9,13.7L17.2,13.4L17,18.2C16.9,18.9 17.4,19.4 18.1,19.5H18.2C18.8,19.5 19.3,19 19.4,18.4L19.6,12.5C19.6,12.2 19.5,11.8 19.3,11.6C19,11.3 18.7,11.2 18.4,11.2M18,5.5A2,2 0 0,0 20,3.5A2,2 0 0,0 18,1.5A2,2 0 0,0 16,3.5A2,2 0 0,0 18,5.5M12.5,21.6C11.6,22.2 10.6,22.5 9.5,22.5C6.5,22.5 4,20 4,17C4,15.9 4.3,14.9 4.9,14L6.4,15.5C6.2,16 6,16.5 6,17C6,18.9 7.6,20.5 9.5,20.5C10.1,20.5 10.6,20.4 11,20.1L12.5,21.6Z" /></svg>');
        background-size: cover;
    }

    :deep().v-slider-thumb__surface::before {
        width: 0%;
        height: 0%;
    }

    :deep().v-slider-thumb__ripple {
        width: 50px;
        height: 50px;
        top: -5px;
        left: -5px;
    }
</style>