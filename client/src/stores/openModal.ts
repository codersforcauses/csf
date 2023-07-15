import { defineStore } from 'pinia'

export const useModalStateStore = defineStore('modalState', {
  state: () => {
    return { modalState: false }
  },
  getters: {
    state: (state: { modalState: boolean }) => state.modalState,
  },
  actions: {
    switchState() {
      this.modalState = !this.modalState
    },
  },
})

