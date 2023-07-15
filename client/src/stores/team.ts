import { defineStore } from 'pinia'
import axios from 'axios'
import snakify, { type Snakify } from 'snakify-ts'
import type { Team } from '@/types/team'
import { useStorage } from '@vueuse/core'
import camelize from 'camelize-ts'
import type { User } from '@/types/user'

const BASE_URL = 'http://localhost:8081/api'

export const useTeamStore = defineStore('team', {
  state: () => ({
    currentTeam: useStorage('team', null as string | null),
    authUser: useStorage('authUser', null as string | null)
  }),

  getters: {
    user: (state) => JSON.parse(state.authUser as string) as User,
    team: (state) => JSON.parse(state.currentTeam as string) as Team
  },

  actions: {
    async getTeams() {
      const teams = await axios.get(`${BASE_URL}/team/all/`).then((res) => {
        if (res.status == 200) {
          return res.data
        }
      })

      return camelize(teams)
    },

    async getTeam(teamId: Number) {
      await axios.get(`${BASE_URL}/team/${teamId}/`).then((res) => {
        if (res.status == 200) {
          const data = camelize(res.data) as Object as Team
          this.currentTeam = JSON.stringify(data)
        }
      })
    },

    async createTeam(data: Omit<Team, 'teamId' | 'joinCode'>) {
      console.log(snakify(data))
      await axios.post(`${BASE_URL}/team/`, snakify(data)).then((res) => {
        if (res.status == 200) {
          const data = camelize(res.data) as Object as Team

          this.currentTeam = JSON.stringify(data)
          this.joinTeam(this.user.id, data.joinCode, true)
        }
      })
    },

    async editTeam(data: Partial<Team>) {
      await axios.patch(`${BASE_URL}/team/`, snakify(data)).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async joinTeam(userId: Number, joinCode: String, teamAdmin: Boolean = false) {
      await axios
        .patch(
          `${BASE_URL}/user/join/${userId}/`,
          snakify({
            joinCode,
            teamAdmin
          })
        )
        .then((res) => {
          if (res.status == 200) {
            const data = camelize(res.data) as Object as User
            console.log(data)
            const { teamId, teamAdmin } = camelize(res.data as Snakify<Partial<User>>)
            this.authUser = JSON.stringify({
              ...this.user,
              teamId,
              teamAdmin
            })
            this.getTeam(teamId as Number)
          }
        })
    },

    async deleteTeam() {
      await axios.delete(`${BASE_URL}/team/delete/${this.user.teamId}/`).then((res) => {
        if (res.status == 200) {
          this.authUser = JSON.stringify({
            ...this.user,
            teamId: null,
            teamAdmin: false
          })
          this.currentTeam = null
        }
      })
    },

    async removeTeam() {
      await axios.patch(`${BASE_URL}/user/remove/${this.user.id}/`).then((res) => {
        if (res.status == 200) {
          this.authUser = JSON.stringify({
            ...this.user,
            teamId: null,
            teamAdmin: false
          })
          this.currentTeam = null
        }
      })
    }
  }
})
