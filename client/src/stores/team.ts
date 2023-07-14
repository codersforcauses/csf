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
      const teams = await axios.get(`${BASE_URL}/team/`).then((res) => {
        if (res.status == 200) {
          return res.data
        }
      })

      return camelize(teams)
    },

    async getTeam(teamId: Number) {
      await axios.get(`${BASE_URL}/team/${teamId}/`).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async createTeam(data: Omit<Team, 'teamId' | 'joinCode'>) {
      console.log(snakify(data))
      await axios.post(`${BASE_URL}/team/`, snakify(data)).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)

          this.joinTeam(this.user.id, this.team.joinCode, true)
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
      const data = {
        userId,
        joinCode,
        teamAdmin
      }
      await axios.patch(`${BASE_URL}/user/join/`, snakify(data)).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async removeTeam(teamId: Number) {
      await axios.delete(`${BASE_URL}/team/${teamId}`).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    }
  }
})
