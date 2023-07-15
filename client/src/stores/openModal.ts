import { defineStore } from 'pinia'

export const useModalStateStore = defineStore('modalState', {
  state: () => ({ modalState: false, destination: '/', redirectOnLogin: false}),
  getters: {
    getState: (state: { modalState: boolean }) => state.modalState,
    getDestination: (state: {destination: string}) => state.destination,
    getRedirectOnLogin: (state: {redirectOnLogin: boolean}) => state.redirectOnLogin,
  },
  actions: {
    switchState() {
      this.modalState = !this.modalState
    },
    changeDestination(path: string) {
        this.destination = path
    },
    switchRedirect() {
        this.redirectOnLogin = !this.redirectOnLogin
    }
  },
})

