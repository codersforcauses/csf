<script setup lang="ts">
import NavbarComponents from './components/NavbarComponents.vue'
import ReloadPWA from './components/ReloadPWA.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <ReloadPWA />
  <NavbarComponents />
  <RouterView />
  <notifications
    classes="my-notification"
    position="bottom right"
    width="450px"
    duration="3"
    closeOnClick="True"
  />
</template>

<style>
body {
  padding-top: 64px;
}

@font-face {
  font-family: 'Hackney';
  src: local('Hackney'), url('./assets/fonts/Hackney-Vector.ttf') format('truetype');
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Black italic.otf') format('opentype');
  font-weight: 900;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Black.otf') format('opentype');
  font-weight: 900;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Bold italic.otf') format('opentype');
  font-weight: 700;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Bold.otf') format('opentype');
  font-weight: 700;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Extra Light italic.otf') format('opentype');
  font-weight: 200;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Extra Light.otf') format('opentype');
  font-weight: 200;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Light italic.otf') format('opentype');
  font-weight: 300;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Light.otf') format('opentype');
  font-weight: 300;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Medium italic.otf') format('opentype');
  font-weight: 500;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Medium.otf') format('opentype');
  font-weight: 500;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Regular italic.otf') format('opentype');
  font-weight: 400;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Regular.otf') format('opentype');
  font-weight: 400;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Semi Bold italic.otf') format('opentype');
  font-weight: 600;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Semi Bold.otf') format('opentype');
  font-weight: 600;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Ultra Light italic.otf') format('opentype');
  font-weight: 100;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Ultra Light.otf') format('opentype');
  font-weight: 100;
}

.my-notification {
  padding: 2%;
  margin-bottom: 5%;
  margin-right: 5%;
  font-size: 15px;
  color: #ffffff;

  .notification-title {
    text-align: center;
  }

  .notification-content {
    text-align: center;
  }

  &.success {
    background: rgb(0, 157, 79);
    border-left-color: rgb(0, 157, 79);
  }

  &.error {
    background: rgb(237, 28, 36);
    border-left-color: rgb(237, 28, 36);
  }
}
</style>
