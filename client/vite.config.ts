import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    VitePWA({
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true
      },
      mode: 'development',
      base: '/',
      srcDir: 'src',
      filename: 'sw.ts',
      includeAssets: ['/favicon.png'],
      strategies: 'injectManifest',
      manifest: {
        name: 'Stride For Education',
        short_name: 'SFE',
        theme_color: '#ffffff',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        icons: [
          {
            src: 'images/CSF_feet_144px.png',
            sizes: '144x144',
            type: 'image/png',
          },
          {
            src: 'images/CSF_feet_144px.png',
            sizes: '144x144',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_512px.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_55_85px.png',
            sizes: '55x85',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_73_113px.png',
            sizes: '73x113',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_110_170px.png',
            sizes: '110x170',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_128_198px.png',
            sizes: '128x198',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_146_227px.png',
            sizes: '146x227',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_165_255px.png',
            sizes: '165x255',
            type: 'image/png',
            purpose: 'maskable'
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
