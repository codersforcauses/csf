import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: null
  }),

  actions: {
    async fetchUser() {},
    async signUp() {},
    async signIn() {}
  }
})
