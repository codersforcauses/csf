<template>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import { useRegisterSW } from 'virtual:pwa-register/vue'
export default defineComponent({
  name: 'ReloadPWA',
  setup() {
    const { offlineReady, needRefresh, updateServiceWorker } = useRegisterSW()
    const close1 = async () => {
      offlineReady.value = false
      needRefresh.value = false
    }
    return { offlineReady, needRefresh, updateServiceWorker, close1 }
  },
  methods: {
    async close() {
      this.offlineReady = false
      this.needRefresh = false
    }
  }
})
</script>
