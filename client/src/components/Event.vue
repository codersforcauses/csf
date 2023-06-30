<template>
    <v-card>
        <v-card-title>
            <span>{{ name }}</span>
            <v-icon v-if="canEdit" icon="mdi-pencil"></v-icon>
            <v-spacer></v-spacer>
            <v-chip variant="outlined" :class="{ 'private-chip': isPrivate, 'official-chip': !isPrivate }">{{ isPrivate ? "Private" : "Official" }}</v-chip>
        </v-card-title>
        <v-card-subtitle>{{ startDate }} - {{ endDate }}</v-card-subtitle>
        <v-card-text>{{ description }}</v-card-text>
    </v-card>
</template>

<script setup lang="ts">
    defineProps(['name','startDate','endDate','description','canEdit', 'isPrivate'])
</script>

<style>
    .v-card-subtitle {
        color: rgb(var(--v-theme-primaryRed));
    }
    .v-card-title {
        display: flex;
    }
    .official-chip {
        color: rgb(var(--v-theme-secondaryGreen));
    }
    .private-chip {
        color: rgb(var(--v-theme-secondaryBlue));
    }
</style>