<script setup lang="ts">
import NavbarComponents from './components/NavbarComponents.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <NavbarComponents />
  </header>
  <RouterView />
</template>

<style>
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
</style>
