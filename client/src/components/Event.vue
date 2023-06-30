<template>
    <v-card>
        <v-card-title>{{ name }} <v-icon icon="mdi-pencil"></v-icon></v-card-title>

        <v-card-subtitle>{{ startDate }} - {{ endDate }}</v-card-subtitle>
        <v-card-text>{{ description }}</v-card-text>
    </v-card>
</template>

<script setup lang="ts">
    defineProps(['name','startDate','endDate','description'])
</script>

<style>
    .v-card-subtitle {
        color: #ED1C24;
    }
</style>