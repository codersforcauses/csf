import { defineStore } from 'pinia'
import axios from 'axios'

const baseUrl = 'http://localhost:8081/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: null,
    token: null
  }),
  getters: {
    user: (state) => state.authUser
  },
  actions: {
    async getToken(username: string, password: string) {
      console.log(`${baseUrl}/auth/token`)
      this.token = await axios.post(`${baseUrl}/auth/token/`, {
        username: username,
        password: password
      })
    },
    async getUser(username: string, password: string) {
      const data = await axios.post(`${baseUrl}/auth/verify/${username}/${password}`)
      if (data.data) {
        // this.getToken()
        this.authUser = data.data
      }
    }
  }
})
