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
    red: 'rgb(237, 28, 36)',
    black: 'rgb(0, 0, 0)',
    white: 'rgb(255, 255, 255)',
    green: 'rgb(0, 157, 79)',
    blue: 'rgb(52, 94, 158)',
    tint: 'rgb(249, 241, 227)'
  }
}

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    themes: {
      csfCustomTheme
    },
    defaultTheme: 'csfCustomTheme'
  },
  icons
})

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
