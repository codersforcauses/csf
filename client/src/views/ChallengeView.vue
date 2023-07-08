<template>
  <div id="header-container" class="text-white pa-lg-12 pa-5">
    <h1 class="text-md-h1 mb-md-10 mb-7 font-weight-medium" id="title">PICK A CHALLENGE</h1>

    <div class="ma-5">
      <h2 style="margin-bottom: 1vh" class="text-subtitle-1 text-md-h6 font-weight-bold">
        Choose your challenge to complete over the 14 days of the challenge
      </h2>
      <h2 class="text-subtitle-1 text-md-h6">
        (Don't worry if you can't hit your daily target, just do your best!)
      </h2>
    </div>
  </div>
  <v-sheet class="d-flex flex-wrap justify-center ma-5">
    <v-card
      class="mx-auto challenge-card pa-3 pa-md-5 card-outer"
      v-bind:style="{
        backgroundImage:
          'linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6)), url(' + challenge.img + ')'
      }"
      theme="dark"
      v-for="challenge in challenges"
      v-bind:key="challenge.title"
    >
      <v-card-title class="text-md-h3 text-h5 font-weight-medium py-2" id="card-head">
        {{ challenge.title }}
      </v-card-title>
      <v-card-text class="text-body-2 text-md-subtitle-1 font-weight-medium py-2">
        {{ challenge.about }}
      </v-card-text>
      <v-card-actions id="bottom">
        <v-list-item class="w-100 pa-3 pa-md-6">
          <template v-slot:append>
            <div>
              <v-icon class="me-1" icon="mdi-map-marker-distance"></v-icon>
              <span class="text-body-2 text-md-subtitle-1 me-2">{{
                challenge.totalkm + 'km'
              }}</span>
              <span class="text-body-2 text-md-subtitle-1 me-1">·</span>
              <v-icon class="me-1" icon="mdi-calendar"></v-icon>
              <span class="text-body-2 text-md-subtitle-1">{{ challenge.km + 'km per day' }}</span>
            </div>
          </template>
        </v-list-item>
      </v-card-actions>
    </v-card>
  </v-sheet>
</template>

<script setup lang="ts">
const challenges = [
  {
    title: 'WOORABINDA CHALLENGE',
    img: '/images/Woorabinda.jpg',
    about: 'Virtually travel the distance from one end of Woorabinda to the other.',
    km: '2',
    totalkm: '24'
  },
  {
    title: 'WURRUMIYANGA CHALLENGE',
    img: '/images/Wurrumiyanga.jpg',
    about: 'Virtually travel the distance around Wurrumiyanga.',
    km: '5',
    totalkm: '60'
  },
  {
    title: "GALIWIN'KU CHALLENGE",
    img: '/images/Galiwin_ku.jpg',
    about: 'Virtually travel the the distance around Galiwin’ku.',
    km: '7',
    totalkm: '84'
  },
  {
    title: 'PALM ISLAND CHALLENGE',
    img: '/images/Palm_Island.jpg',
    about: 'Virtually travel the length of Palm Island.',
    km: '10',
    totalkm: '120'
  }
]
</script>

<style>
@media only screen and (max-width: 800px) {
  .challenge-card {
    width: 80vw;
    margin: 2.5vw;
    height: 25vh;
  }
}

@media only screen and (min-width: 800px) {
  .challenge-card {
    width: 40vw;
    margin: 2vh;
    height: 30vh;
  }
}

#title {
  font-family: 'Hackney' !important;
  line-height: 1.2em;
}

.challenge-image {
  width: 1000;
}

.challenge-card {
  box-shadow: 0 2px 7px rgb(0 0 0 / 0.1);
  background-size: cover;
  background-position: 100%, 0;
}

#header-container {
  text-align: center;
  background-color: #f9f1e3;
  background-image: url('../../public/images/Footer-min.jpeg');
  background-repeat: repeat;
  background-size: cover;
}

#header-container h1 {
  font-size: 4rem;
  font-weight: contain;
}

#header-contents {
  font-family: 'Sofia Pro';
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
}

#card-head {
  font-family: 'Hackney' !important;
}
</style>
