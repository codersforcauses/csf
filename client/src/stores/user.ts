import { defineStore } from 'pinia'
import axios from 'axios'
import { useStorage } from '@vueuse/core'
import type { User } from '@/types/user'

const BASE_URL = 'http://localhost:8081/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: useStorage('authUser', null as User | null | String),
    authToken: useStorage('authToken', null as string | null)
  }),
  getters: {
    user: (state) => state.authUser,
    token: (state) => JSON.parse(state.authToken as string)
  },
  actions: {
    logout() {
      this.authUser = null
      this.authToken = null
    },

    async loginUser(username: string, password: string) {
      try {
        await axios
          .post(`${BASE_URL}/auth/token/`, {
            username: username,
            password: password
          })
          .then((res) => {
            if (res.status == 200) {
              // this.getUser(username)
              this.authUser = username
              this.authToken = JSON.stringify(res.data)
            }
          })
      } catch (error) {
        this.authUser = null
        this.authToken = null
      }
    },

    async getUser(username: String) {
      await axios.get(`${BASE_URL}/user/${username}/`).then((res) => {
        if (res.status == 200) this.authUser = res.data
      })
    }
  }
})
