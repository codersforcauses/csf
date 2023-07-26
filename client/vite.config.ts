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
            src: 'images/CSF_feet_144_sq_px.png',
            sizes: '144x144',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_72_72px.png',
            sizes: '72x72',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_96_96px.png',
            sizes: '96x96',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_120_120px.png',
            sizes: '120x120',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_152_152px.png',
            sizes: '152x152',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_167_167px.png',
            sizes: '167x167',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_192_192px.png',
            sizes: '192x192',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_384_384px.png',
            sizes: '384x384',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'images/CSF_feet_512_512px.png',
            sizes: '512x512',
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
