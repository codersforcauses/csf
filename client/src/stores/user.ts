import { defineStore } from 'pinia'
import axios from 'axios'

const baseUrl = 'https://localhost:8081'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null
  }),
  getters: {
    user: (state) => state.user
  },
  actions: {
    async getToken(username: string) {
      await axios.get(`${baseUrl}/token/${username}`)
    },
    async getUser(username: string, password: string) {
      const data = await axios.get(`${baseUrl}/user/${username}/${password}`)
      if (data.data) {
        this.getToken(username)
        this.user = data.data
      }
    }
  }
})

// export const useUserStore = defineStore('user', () => {
//   const user = ref(null)
//   const token = ref(null)

//   const userLogin = computed(async (username: string, password: string) => {
//     const res = await fetch(`${baseUrl}/signin`, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify({ username, password })
//     })
//     user.value = await res.json()
//     return user
//   })

//   return { user, token, userLogin }

//   // state: () => ({
//   //   user: null,
//   //   token: null
//   // }),
//   // actions: {
//   //   async fetchUser() {
//   //     const res = await fetch(`${baseUrl}/user`)
//   //     const user = await res.json()
//   //     this.user = user
//   //   },
//   //   async signUp(username: string, password: string) {
//   //     const res = await fetch(`${baseUrl}/register`, {
//   //       method: 'POST',
//   //       headers: {
//   //         'Content-Type': 'application/json'
//   //       },
//   //       body: JSON.stringify({ username, password })
//   //     })
//   //     const user = await res.json()
//   //     this.user = user
//   //   },
//   //   async signIn(username: string, password: string) {
//   //     const res = await fetch(`${baseUrl}/signin`, {
//   //       method: 'POST',
//   //       headers: {
//   //         'Content-Type': 'application/json'
//   //       },
//   //       body: JSON.stringify({ username, password })
//   //     })
//   //     const user = await res.json()
//   //     this.user = user
//   //   }
//   // }
// })
