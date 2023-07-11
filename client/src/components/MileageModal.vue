<template>
    <v-dialog v-model="value" :fullscreen="xs" width="500px">
        <v-card height="800px">
            <div style="height:8px">
                <v-img src="/images/Footer-min.jpeg" width="100%" cover />
            </div>
            <v-card-title class="ma-auto text-h5">Add Mileage</v-card-title>
            <v-card-text>
                <v-row>
                    <v-col>
                        <v-text-field
                            type="date"
                            label="Date"
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-slider
                            v-model="distance"
                            color="green"
                            :thumb-size="40"
                            elevation="0"
                            :step="1"
                            min="1"
                            max="100"
                        />
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
            <v-card-action>
                <v-btn @click="$emit('update:modelValue', !modelValue)">CLOSE</v-btn>
            </v-card-action>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
    import { useDisplay} from 'vuetify'
    import { computed } from 'vue'
    import { ref } from 'vue'
    
    const { xs } = useDisplay()
    const props = defineProps(['modelValue'])
    const emit = defineEmits(['update:modelValue', 'handleSubmit'])
    const distance = ref(1)

    const value = computed({
        get() {
            return props.modelValue
        },
        set(value) {
            emit('update:modelValue', value)
        }
    })
</script>

<style scoped>
    :deep().v-slider-thumb__surface {
        border-radius: 0% !important; 
        background-color: transparent !important;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>run</title><path d="M13.5,5.5C14.59,5.5 15.5,4.58 15.5,3.5C15.5,2.38 14.59,1.5 13.5,1.5C12.39,1.5 11.5,2.38 11.5,3.5C11.5,4.58 12.39,5.5 13.5,5.5M9.89,19.38L10.89,15L13,17V23H15V15.5L12.89,13.5L13.5,10.5C14.79,12 16.79,13 19,13V11C17.09,11 15.5,10 14.69,8.58L13.69,7C13.29,6.38 12.69,6 12,6C11.69,6 11.5,6.08 11.19,6.08L6,8.28V13H8V9.58L9.79,8.88L8.19,17L3.29,16L2.89,18L9.89,19.38Z" /></svg>');
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