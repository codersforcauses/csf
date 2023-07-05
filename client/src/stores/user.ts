import { defineStore } from 'pinia'
import axios from 'axios'
import { useStorage } from '@vueuse/core'

const BASE_URL = 'http://localhost:8081/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: useStorage('authUser', null as string | null),
    authToken: useStorage('authToken', null as string | null)
  }),
  getters: {
    user: (state) => state.authUser,
    token: (state) => JSON.parse(state.authToken as string)
  },
  actions: {
    async loginUser(username: string, password: string) {
      try {
        await axios
          .post(`${BASE_URL}/auth/token/`, {
            username: username,
            password: password
          })
          .then((res) => {
            if (res.status == 200) {
              this.authUser = username
              this.authToken = JSON.stringify(res.data)
            }
          })
      } catch (error) {
        this.authUser = null
        this.authToken = null
      }
    },
    async registerUser(firstname : string, lastname: string, email: string) {
      try {
        await axios
          .post(`${BASE_URL}/users/register/`, {
            firstname: firstname,
            lastname: lastname,
            email: email
          })
          .then((res) => {
            if (res.status == 200) {
              // this.authUser = username
              this.authToken = JSON.stringify(res.data)
              console.log("success")
            }
          })
      } catch (error) {
        // this.authUser = null
        this.authToken = null
      }
  }
}
})