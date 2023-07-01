<template>
    <v-card>
        <v-card-title>
            <span>{{ name }}</span>
            <v-icon v-if="canEdit" icon="mdi-pencil"></v-icon>
            <v-spacer></v-spacer>
            <v-chip variant="outlined" :class="{ 'text-secondaryGreen': isPrivate, 'text-secondaryBlue': !isPrivate }">{{ isPrivate ? "Private" : "Official" }}</v-chip>
        </v-card-title>
        <v-card-subtitle class="text-primaryRed">{{ startDate }} - {{ endDate }}</v-card-subtitle>
        <v-card-text>{{ description }}</v-card-text>
    </v-card>
</template>

<script setup lang="ts">
    interface Props {
        name: string
        startDate: string
        endDate: string
        description: string
        canEdit: boolean
        isPrivate: boolean
    }
    defineProps<Props>()
</script>

<style>
    .v-card-title {
        display: flex;
    }
</style>