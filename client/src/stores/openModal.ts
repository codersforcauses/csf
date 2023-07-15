import { defineStore } from 'pinia'

export const useModalStateStore = defineStore('modalState', {
  state: () => ({ modalState: false }),
  getters: {
    getState: (state: { modalState: boolean }) => state.modalState,
  },
  actions: {
    switchState() {
      this.modalState = !this.modalState
    },
  },
})

