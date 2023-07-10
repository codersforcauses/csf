import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'

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
        await server
          .post('auth/token/', {
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
    async registerUser(obj: object) {
      await server.post('auth/register/', obj)
    }
  }
})
