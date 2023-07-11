import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type { User } from '@/types/user'
import camelize from 'camelize-ts'
import { type Snakify } from 'snakify-ts'

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
        await server
          .post('auth/token/', {
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
        return await server
        .patch(`user/change_password/${this.user.id}`, {
          password: newPassword,
        }).then((res) => {
          return res.status
        })
      }
    },
    async sendResetEmail(email: string) {
      return await server
        .post('user/request_reset_password/', {
          email: email
        })
        .then((res) => {
          if (res.status === 200 && res.data !== 'unregistered') {
            console.log(res.data) // log in place of emailing for now
          }
          return res.status
        })
    },
    async submitResetToken(token: string) {
      return await server
        .post('user/verify_token/', {
          reset_token: token
        })
        .then((res) => {
          return res.status
        })
    },
    async submitNewPassword(token: string, newPassword: string) {
      return await server
        .post('user/reset_password/', {
          reset_token: token,
          password: newPassword
        })
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
    }
  }
})
