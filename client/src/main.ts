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

const app = createApp(App)

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
    primaryForm: 'rgb(236,236,236)'
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

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
