import { defineStore } from 'pinia'
import server from '@/utils/server'
import type { Signup, Tokens, User, UserSettings } from '@/types/user'
import camelize from 'camelize-ts'
import snakify from 'snakify-ts'
import useNullableStorage from '@/utils/useNullableStorage'
import { useTeamStore } from './team'
import { useMileageStore } from './mileage'

export const useUserStore = defineStore('user', () => {
  const user = useNullableStorage<User>('authUser')
  const token = useNullableStorage<Tokens>('authToken')

  if (token.value != null)
    server.defaults.headers.common['Authorization'] = 'Bearer ' + token.value.access

  return {
    user,

    logout() {
      user.value = null
      token.value = null
      useTeamStore().team = null
      useMileageStore().recentMileage = []
      delete server.defaults.headers.common['Authorization']
    },

    async getUser(username: string) {
      const { status, data } = await server.get(`user/${username}/`)
      if (status == 200) user.value = camelize<User>(data)
    },

    async login(username: string, password: string) {
      const { status, data } = await server.post(
        'auth/token/',
        { username, password },
        { validateStatus: () => true }
      )
      if (status == 200) {
        await this.getUser(username)
        token.value = data
        server.defaults.headers.common['Authorization'] = 'Bearer ' + data.access
        return true
      }
      return false
    },

    async changePassword(oldPassword: string, newPassword: string) {
      if (user.value) {
        return await server
          .patch(
            `user/change_password/${user.value.id}`,
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
        .patch(`user/change_details/${user.value!.id}`, snakify(newDetails))
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

    async registerUser(signup: Signup) {
      await server.post('auth/register/', snakify(signup))
    },

    async checkToken() {
      if (token.value != null) {
        const parts = token.value.access.split('.')
        const payload = JSON.parse(atob(parts[1]))
        const left = payload.exp - Date.now() / 1000
        if (left < 0) {
          const { status, data } = await server.post('http://localhost:8081/api/auth/refresh/', {
            refresh: token.value.refresh
          })
          if (status == 200) token.value.access = data.access
        }
      }
    }
  }
})
