<template>
    <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0 bg-primaryWhite" align="center">
        <v-col>
            <h1>Welcome back, {{ tempUserFirstName }}!</h1>
            <!-- <v-card variant="flat">
                <v-card-title class="pa-0">Welcome back, {{ tempUserFirstName }}!</v-card-title>
            </v-card> -->
        </v-col>
    </v-row>
    <v-divider/>
    <v-row class="ma-0 pl-4 pr-4 pb-0 pt-0" align="center">
        <v-col>
            <v-card variant="flat" class="pb-2 pr-2">
                <v-container class="ma-0 pa-0" fluid>
                    <v-row>
                        <v-col cols="auto">
                            <v-icon icon="mdi-run-fast" size="52"/>
                        </v-col>
                        <v-col>
                            <v-chip color="green" class="rounded text-h5">{{ tempUserMileage }} KM</v-chip>
                            <v-card-subtitle>TOTAL</v-card-subtitle>
                        </v-col>
                        <v-spacer/>
                        <v-col cols="auto">
                            <v-btn variant="elevated" color="primaryRed" icon="mdi-plus" size="large" elevation="4"></v-btn>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card>
        </v-col>
    </v-row>
    <v-divider/>
    <v-row class="ma-0" align="center">
        <v-col>
            <v-card variant="flat">
                <v-card-title>Mileage Graph</v-card-title>
                <mileage-graph :labels="tempLabels" :datasets="tempDatasets"/>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup lang="ts">
    import { ref } from "vue"
    import MileageGraph from "@/components/MileageGraph.vue";

    const tempIsLoggedIn = ref(true)
    const tempUserFirstName = ref("John")
    const tempUserMileage = ref(100)
    const tempLabels = ref(["January", "February", "March", "April", "May", "June", "July"])
    const tempDatasets = ref([
        {
            label: 'Yearly Mileage',
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40]
        }
    ])


</script>

<style scoped></style>