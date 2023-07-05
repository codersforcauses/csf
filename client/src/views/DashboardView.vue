<template>
    <v-row align="center">
        <v-col>
            <v-card variant="flat">
                <v-card-title>Welcome back, {{ tempUserFirstName }}!</v-card-title>
            </v-card>
        </v-col>
    </v-row>
    <v-divider/>
    <v-row class="pl-4 pr-4">
        <v-col>
            <v-card variant="flat">
                <v-row>
                    <v-col>
                        <v-icon icon="mdi-run"/>
                    </v-col>
                    <v-col>
                        <v-card-title style="background-color: rgba(0, 157, 79, 0.19);">{{ tempUserMileage }} KM</v-card-title>
                        <v-card-subtitle>TOTAL</v-card-subtitle>
                    </v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>
    <v-divider/>
    <v-row class="pl-4 pr-4">
        <v-col>
            <v-card variant="flat">
                <v-card-title>Mileage Graph</v-card-title>
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