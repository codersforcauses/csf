import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx(), VitePWA({
    registerType: 'autoUpdate',
    devOptions: {
      enabled: true
    },
    mode: "development",
    base: "/",
    srcDir: "src",
    filename: "sw.ts",
    includeAssets: ["/favicon.png"],
    strategies: "injectManifest",
    manifest: {
      name: "Stride For Education",
      short_name: "Stride For Education",
      theme_color: "#ffffff",
      start_url: "/",
      display: "standalone",
      background_color: "#ffffff",
      icons: [
        // {
        //   src: "public/images/CSF_Logo_WHITE.png",
        //   sizes: "192x192",
        //   type: "image/png",
        // },
        // {
        //   src: "/icon-512.png",
        //   sizes: "512x512",
        //   type: "image/png",
        // },
        // {
        //   src: "icon-512.png",
        //   sizes: "512x512",
        //   type: "image/png",
        //   purpose: "any maskable",
        // },
        // {
        //   src: "public/images/CSF_Logo_WHITE.png",
        //   sizes: "512x512",
        //   type: "image/png",
        //   purpose: "any maskable",
        // },
        {
          src: "images/CSF_144px.png",
          sizes: "144x144",
          type: "image/png",
        },
        {
          src: "images/CSF_144px.png",
          sizes: "144x144",
          type: "image/png",
          purpose: "maskable",
        },
        {
          src: "images/CSF_Logo_WHITE.png",
          sizes: "842x425",
          type: "image/png",
          purpose: "maskable"
        },
        
      ],
    },
  })
],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
