import { defineStore } from 'pinia'
import axios from 'axios'

const baseUrl = 'http://localhost:8081/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: null as string | null
  }),
  getters: {
    user: (state) => state.authUser
  },
  actions: {
    async loginUser(username: string, password: string) {
      try {
        await axios
          .post(`${baseUrl}/auth/token/`, {
            username: username,
            password: password
          })
          .then((res) => {
            if (res.status == 200) {
              this.authUser = username
            }
          })
      } catch (error) {
        return error
      }
    }
  }
})
