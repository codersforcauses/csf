<template>
    <v-dialog v-model="dialog" :fullscreen="mobile" max-width="912px">
        <v-card>
            <div style="height:8px">
                <v-img src="/images/Footer-min.jpeg" width="100%" cover />
            </div>
            <v-card-title>Add Mileage</v-card-title>
        </v-card>

    </v-dialog>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { useDisplay} from 'vuetify'
    
    const { mobile } = useDisplay()
    const dialog = ref<boolean>(false)
    const props = defineProps('modelValue')
    const emits = defineEmits('update:modelValue', 'handleSubmit')
</script>

<style scoped></style>