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
    async changePassword(newPassword: string) {
      return axios
        .patch(`${BASE_URL}/users/change_password/`, {
          username: this.authUser,
          password: newPassword,
        })
        .then((res) => {
          if (res.status == 200) {
            return res.data
          }
        })
    },
    async sendResetEmail(email: string) {
      axios
        .post(`${BASE_URL}/users/request_reset_password/`, {
          email: email
        })
        .then((res) => {
          if (res.status == 200) {
            console.log(res.data);
          }
        })
    },
    async submitResetToken(token: string) {
      return axios
        .post(`${BASE_URL}/users/verify_token/`, {
          reset_token: token
        })
        .then((res) => {
          return res.data
        })
    },
    async submitNewPassword(token: string, newPassword: string) {
      return axios
        .post(`${BASE_URL}/users/reset_password/`, {
          reset_token: token,
          password: newPassword
        })
        .then((res) => {
          if (res.status == 200) {
            console.log(res.data);
          }
        })
    },
    async registerUser(obj: object) {
      await axios.post(`${BASE_URL}/auth/register/`, obj)
    }
  }
})
