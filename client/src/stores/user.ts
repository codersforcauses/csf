import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import axios from 'axios'
import type { Tokens, User, UserSettings } from '@/types/user'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'
// import { base64url, jwtDecrypt } from 'jose'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: useStorage('authUser', null as string | null),
    authToken: useStorage('authToken', null as string | null)
  }),
  getters: {
    user: (state) => (state.authUser ? (JSON.parse(state.authUser) as User) : null),
    token: (state) => (state.authToken ? (JSON.parse(state.authToken) as Tokens) : null)
  },
  actions: {
    logout() {
      this.authUser = null
      this.authToken = null
    },

    async loginUser(username: string, password: string) {
      return await server
        .post('auth/token/', {
          username: username,
          password: password
        })
        .then(async (res) => {
          if (res.status == 200) {
            await this.getUser(username)
            this.authToken = JSON.stringify(res.data)
            return true
          }
        })
        .catch((error) => {
          console.log(error)

          this.authToken = null
          this.authUser = null
          return false
        })
    },
    async changePassword(oldPassword: string, newPassword: string) {
      if (this.user) {
        return await server
          .patch(
            `user/change_password/${this.user.id}`,
            snakify({
              oldPassword: oldPassword,
              password: newPassword
            })
          )
          .then((res) => {
            return res.status
          })
      }
    },
    async changeDetails(newDetails: UserSettings) {
      return await server
        .patch(`user/change_details/${this.user!.id}`, snakify(newDetails))
        .then((res) => {
          return res.status
        })
    },
    async sendResetEmail(email: string) {
      return await server
        .post('user/request_reset_password/', {
          email: email
        })
        .then((res) => {
          return res.status
        })
    },
    async submitResetToken(token: string) {
      return await server
        .post(
          'user/verify_token/',
          snakify({
            resetToken: token
          })
        )
        .then((res) => {
          return res.status
        })
    },
    async submitNewPassword(token: string, newPassword: string) {
      return await server
        .post(
          'user/reset_password/',
          snakify({
            resetToken: token,
            password: newPassword
          })
        )
        .then((res) => {
          return res.status
        })
    },

    async getUser(username: string) {
      await server.get(`user/${username}/`).then((res) => {
        if (res.status == 200) {
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
          } = camelize(res.data as Snakify<User>)

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
      await server.post('auth/register/', obj)
    },

    async checkToken() {
      if (this.token != null) {
        const parts = this.token.access.split('.')
        const payload = JSON.parse(atob(parts[1]))
        const left = payload.exp - Date.now() / 1000
        if (left < 0) {
          const { status, data } = await axios.post('http://localhost:8081/api/auth/refresh/', {
            refresh: this.token.refresh
          })
          if (status == 200) this.token.access = data.access
        }
      }
    }
  }
})
