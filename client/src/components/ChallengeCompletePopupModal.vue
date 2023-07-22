<template>
    <v-dialog v-model="value" :fullscreen="isFullscreen" max-width="500">
        <v-card>
            <div style="height: 8px">
                <v-img src="/images/Footer-min.jpeg" width="100%" alt="red background" cover />
            </div>
            <v-card-item class="d-flex justify-center">
                <v-card-title class="d-flex justify-center">
                    Congratulations!
                </v-card-title>
                <v-card-subtitle>You completed the {{ challengeName }} challenge!</v-card-subtitle>
            </v-card-item>
            <v-card-actions class="d-flex justify-end">
                <v-btn @click="$emit('update:modelValue', !modelValue)">CLOSE</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
    import { ref, computed } from 'vue'

    const isFullscreen = ref(false)
    const emit = defineEmits(['update:modelValue'])
    const props = defineProps(['modelValue', 'challengeName'])

    const value = computed({
        get() {
            return props.modelValue
        },
        set(value) {
            emit('update:modelValue', value)
        }
    })
</script>

<style scoped></style>