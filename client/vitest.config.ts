import { fileURLToPath } from 'node:url'
import { mergeConfig } from 'vite'
import { configDefaults, defineConfig as defineVitestConfig } from 'vitest/config'
import viteConfig from './vite.config'
import viteCompression from 'vite-plugin-compression'
import { defineConfig as defineViteConfig } from 'vite'

const vitestConfig = defineVitestConfig({
  test: {
    environment: 'jsdom',
    exclude: [...configDefaults.exclude, 'e2e/*'],
    root: fileURLToPath(new URL('./', import.meta.url)),
    transformMode: {
      web: [/\.[jt]sx$/]
    }
  }
});

const finalViteConfig = defineViteConfig({
  ...viteConfig,
  plugins: [
    viteCompression(),
  ],
});

export default mergeConfig(finalViteConfig, vitestConfig);
