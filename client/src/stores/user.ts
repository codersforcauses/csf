import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type { User } from '@/types/user'
import camelize from 'camelize-ts'
import { Snakify } from 'snakify-ts'

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
