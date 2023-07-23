import { defineStore } from 'pinia'
import server from '@/utils/server'
import type { Signup, Tokens, User, UserSettings } from '@/types/user'
import camelize from 'camelize-ts'
import snakify from 'snakify-ts'
import { useTeamStore } from './team'
import { useMileageStore } from './mileage'
import useNullableStorage from '@/utils/useNullableStorage'
import { useModalStore } from './modal'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: useNullableStorage<User>('authUser'),
    token: useNullableStorage<Tokens>('authToken')
  }),

  actions: {
    logout() {
      this.user = null
      this.token = null
      useTeamStore().team = null
    },

    async getUser(username: string) {
      const { status, data } = await server.get(`user/${username}/`)
      if (status == 200) this.user = camelize<User>(data)
    },

    async login(username: string, password: string) {
      const { status, data } = await server.post(
        'auth/token/',
        { username, password },
        { validateStatus: () => true }
      )
      if (status == 200) {
        await this.getUser(username)
        this.token = data
        return true
      }
      return false
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

    async registerUser(signup: Signup) {
      await server.post('auth/register/', snakify(signup))
    },

    async refreshToken() {
      if (this.token != null) {
        const { status, data } = await server.post('auth/refresh/', {refresh: this.token.refresh}, { validateStatus: () => true})
        if (status == 200) {
          this.token.access = data.access
          return true
        }
        this.logout()
        useModalStore().login()
      }
      return false
    }
  }
})
