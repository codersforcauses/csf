import { defineStore } from 'pinia'
import axios from 'axios'

const baseUrl = 'https://localhost:8081'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null
  }),
  getters: {
    user: (state) => state.user
  },
  actions: {
    async getToken(username: string) {
      await axios.get(`${baseUrl}/token/${username}`)
    },
    async getUser(username: string, password: string) {
      const data = await axios.get(`${baseUrl}/user/${username}/${password}`)
      if (data.data) {
        this.getToken(username)
        this.user = data.data
      }
    }
  }
})
