import { defineStore } from 'pinia'
import axios from 'axios'
import { useStorage } from '@vueuse/core'
import type { User } from '@/types/user'
import camelize from 'camelize-ts'

const BASE_URL = 'http://localhost:8081/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: useStorage('authUser', null as string | null),
    authToken: useStorage('authToken', null as string | null)
  }),
  getters: {
    user: (state) => JSON.parse(state.authUser as string) as User,
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
              this.getUser(username)
              this.authToken = JSON.stringify(res.data)
            }
          })
      } catch (error) {
        this.authUser = null
        this.authToken = null
      }
    },
    async changePassword(newPassword: string) {
      if (this.user) {
        return await axios
        .patch(`${BASE_URL}/user/change_password/${this.user.id}`, {
          password: newPassword,
        }).then((res) => {
          return res.status
        })
      }
    },
    async sendResetEmail(email: string) {
      return axios
        .post(`${BASE_URL}/user/request_reset_password/`, {
          email: email
        })
        .then((res) => {
          if (res.status === 200) {
            console.log(res.data)
          }
          return res.status
        })
    },
    async submitResetToken(token: string) {
      return axios
        .post(`${BASE_URL}/user/verify_token/`, {
          reset_token: token
        })
        .then((res) => {
          return res.status
        })
    },
    async submitNewPassword(token: string, newPassword: string) {
      return axios
        .post(`${BASE_URL}/user/reset_password/`, {
          reset_token: token,
          password: newPassword
        })
        .then((res) => {
          return res.status
        })
    },

    async getUser(username: String) {
      await axios.get(`${BASE_URL}/user/${username}/`).then((res) => {
        if (res.status == 200) {
          const data = camelize(res.data) as Object as User
          const {
            id,
            username,
            firstName,
            lastName,
            email,
            avatar,
            travelMethod,
            teamSignup,
            hasConsent,
            subteamId,
            teamId,
            teamAdmin
          } = data

          this.authUser = JSON.stringify({
            id,
            username,
            firstName,
            lastName,
            email,
            avatar,
            travelMethod,
            teamSignup,
            hasConsent,
            subteamId,
            teamId,
            teamAdmin
          })
        }
      })
    },

    async registerUser(obj: object) {
      await axios.post(`${BASE_URL}/auth/register/`, obj)
    }
  }
})
