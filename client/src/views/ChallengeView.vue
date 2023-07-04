<template>
    <div id="header-container" class="text-white">
        <h1 class="text-md-h1 mt-10 mb-10">Challenges</h1>

        <div class="ma-10">
            <h2 style="margin-bottom: 1vh;" class="text-h6">Choose your challenge to complete over the 12 days of the
                challenge</h2>
            <h2 class="text-h6">(Don't worry if you can't hit your daily target, just do your best!)</h2>
        </div>
    </div>
    <v-sheet class="d-flex flex-wrap justify-center">
        <v-card class="mx-auto challenge-card pa-5 card-outer" v-bind:style="{ backgroundImage: 'url(' + challenge.img + ')' }" theme="dark" v-for="challenge in challenges">
            <v-card-title class="text-lg-h5 py-2">
                {{ challenge.title }}
            </v-card-title>
            <v-card-text class="text-subtitle-1 py-2">
                {{challenge.about}}
            </v-card-text>
            <v-card-actions id="bottom">
                <v-list-item class="w-100 pa-6">
                    <template v-slot:append>
                        <div>
                            <v-icon class="me-1" icon="mdi-map-marker-distance"></v-icon>
                            <span class="subheading me-2">{{challenge.totalkm + "km"}}</span>
                            <span class="me-1">·</span>
                            <v-icon class="me-1" icon="mdi-calendar"></v-icon>
                            <span class="subheading">{{challenge.km + "km per day"}}</span>
                        </div>
                    </template>
                </v-list-item>
            </v-card-actions>
        </v-card>

    </v-sheet>
</template>

<script setup lang="ts">
const challenges = [
    { title: "WOORABINDA CHALLENGE", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "Virtually travel the distance from one end of Woorabinda to the other.", km: "2", totalkm: "24" },
    { title: "WURRUMIYANGA CHALLENGE", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "Virtually travel the distance around Wurrumiyanga.", km: "5", totalkm: "60" },
    { title: "GALIWIN'KU CHALLENGE", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "Virtually travel the the distance around Galiwin’ku.", km: "7", totalkm: "84" },
    { title: "PALM ISLAND CHALLENGE", img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg", about: "Virtually travel the length of Palm Island.", km: "10", totalkm: "120" }
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
        margin: 2vh;
    }
}

.challenge-image {
    width: 1000
}

.challenge-card {
    box-shadow: 0 2px 7px rgb(0 0 0 / 0.1);
    height: 35vh;
}

#header-container {
    text-align: center;
    background-color: #f9f1e3;
    padding: 9vh;
    margin-bottom: 3vh;
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

#bottom {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 100%;
    background-color: black;
    opacity: 80%;
}
</style>
  