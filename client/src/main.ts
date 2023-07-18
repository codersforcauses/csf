import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import type { ThemeDefinition } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import * as icons from 'vuetify/iconsets/mdi-svg'

import App from './App.vue'
import router from './router'

import Notifications from '@kyvg/vue3-notification'

const csfCustomTheme: ThemeDefinition = {
  dark: false,
  colors: {
    primaryRed: 'rgb(237, 28, 36)',
    primaryBlack: 'rgb(0, 0, 0)',
    primaryWhite: 'rgb(255, 255, 255)',
    secondaryGreen: 'rgb(0, 157, 79)',
    secondaryBlue: 'rgb(52, 94, 158)',
    secondaryTint: 'rgb(249, 241, 227)',
    secondaryGrey: 'rgb(32,32,32)',
    backgroundGrey: 'rgb(236,236,236)'
  }
}

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'csfCustomTheme',
    themes: {
      csfCustomTheme
    }
  },
  icons
})

createApp(App).use(createPinia()).use(router).use(vuetify).use(Notifications).mount('#app')
