<template>
    <v-row class="ma-0 pl-4 pr-4 pt-4 pb-0" align="center">
        <v-col>
            <v-card variant="flat">
                <v-card-title class="pa-0">Welcome back, {{ tempUserFirstName }}!</v-card-title>
            </v-card>
        </v-col>
    </v-row>
    <v-divider/>
    <v-row class="ma-0 pl-4 pr-4 pb-0 pt-0" align="center">
        <v-col>
            <v-card variant="outlined">
                <v-row>
                    <v-col cols="auto">
                        <v-icon icon="mdi-run-fast" size="48"/>
                    </v-col>
                    <v-col>
                        <v-chip color="green" class="rounded text-h6">{{ tempUserMileage }} KM</v-chip>
                        <v-card-subtitle>TOTAL</v-card-subtitle>
                    </v-col>
                    <v-spacer/>
                    <v-col>
                        ADD
                    </v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup lang="ts">
    import { ref } from "vue"

    const tempIsLoggedIn = ref(true)
    const tempUserFirstName = ref("John")
    const tempUserMileage = ref(100)
</script>

<style scoped></style>