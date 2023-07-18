import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type { User, UserSettings } from '@/types/user'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'
import { type AxiosRequestConfig } from 'axios'
import { base64url, jwtDecrypt } from 'jose'

export const useUserStore = defineStore('user', {
  state: () => ({
    authUser: useStorage('authUser', null as string | null),
    authToken: useStorage('authToken', null as string | null)
  }),
  getters: {
    user: (state) => (state.authUser ? (JSON.parse(state.authUser) as User) : null),
    token: (state) => (state.authToken ? JSON.parse(state.authToken) : null)
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
        .catch(() => {
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

    async refreshToken(token: string) {
      // const test = process.env.SECRET_KEY;
      //
      // console.log(import.meta.env.VITE_SECRET);

      // console.log(import.meta.);
      const secret = import.meta.env.VITE_SECRET as string
      const jwt =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5NTg3ODkxLCJpYXQiOjE2ODk1ODc1OTEsImp0aSI6IjhlMTNhYzdhNmMwODRmMDJhYTVhNTBkMjAzNWQwNWU0IiwidXNlcl9pZCI6Mn0.NDGRVje0J3YyFzxq5qxBbjD-5n-Wiv3nywAs4qFsCqw'
      // const data = JSON.parse(this.authToken?.toString() as string) as Tokens
      // console.log(data.access)

      const { payload, protectedHeader } = await jwtDecrypt(jwt, secret, {
        issuer: 'urn:example:issuer',
        audience: 'urn:example:audience'
      })
      console.log(protectedHeader)
      console.log(payload)
      //   const headers: AxiosRequestConfig['headers'] = {
      //     refresh: token
      //   }

      //   await server
      //     .post('auth/refresh/', headers)
      //     .then((res) => {
      //       data.access = res.data.access
      //     })
      //     .catch((error) => {
      //       console.log(error)
      //     })

      //   this.authToken = JSON.stringify(data);
    }
  }
})
