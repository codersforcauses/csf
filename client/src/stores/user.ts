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
    async registerUser(first_name : string, last_name: string, email: string) {
      try {
        await axios
          .post(`${BASE_URL}/users/register/`, {
            first_name: first_name,
            last_name: last_name,
            email: email
          })
      } catch (error) {
        console.log(error)
      }
  }
}
})