import { defineStore } from 'pinia'

export const useModalStateStore = defineStore('modalState', {
  state: () => {
    return { modalState: false }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    switchState() {
      this.modalState = !this.modalState
    },
  },
})

