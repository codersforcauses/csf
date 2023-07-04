<template>
    <div id="header-container" class="text-white">
        <h1 class="text-md-h1 mt-10 mb-10">Challenges</h1>

        <div class="ma-4">
            <h2 style="margin-bottom: 1vh;" class="text-h6">Choose your challenge to complete over the 12 days of the challenge</h2>
            <h2 class="text-h6">(Don't worry if you can't hit your daily target, just do your best!)</h2>
        </div>
    </div>
    <v-sheet class="d-flex flex-wrap justify-center">
        <v-card class="pa-2 align-self-auto challenge-card dark" v-for="challenge in challenges" v-bind:style="{ backgroundImage: 'url(' + challenge.img + ')' }" style>
            <v-title class="text-h4">{{ challenge.title }}</v-title>
        </v-card>

    </v-sheet>
</template>

<script setup lang="ts">
const challenges = [
    { title: "card1", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "some text", km: "", totalkm: ""},
    { title: "card1", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "some text", km: "", totalkm: ""},
    { title: "card1", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "some text", km: "", totalkm: ""},
    { title: "card1", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "some text", km: "", totalkm: ""}
]

</script>
  
<style>
@media only screen and (max-width: 800px) {
    .challenge-card {
        width: 80vw;
        margin: 2.5vw;
    }
}

@media only screen and (min-width: 800px) {
    .challenge-card {
        width: 40vw;
        height: 35vh;
        margin: 2vh;
    }
}

.challenge-image {
    width: 1000
}

.challenge-card {
    box-shadow: 0 2px 7px rgb(0 0 0 / 0.1);
}

#header-container {
    text-align: center;
    background-color: #f9f1e3;
    padding: 4vh;
    margin-bottom: 1vh;
    background-image: url('../../public/images/Footer-min.jpeg');
    background-repeat: repeat;
    background-size: cover;
}

#header-container h1 {
    font-size: 4rem;
    font-weight: contain;
}

#header-contents {
    margin: 4vh;
}

.challenge-card:hover {
    transition-duration: 0.3s;
    box-shadow: 0 4px 12px rgb(0 0 0 / 0.2);
}
</style>
  