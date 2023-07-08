import { defineStore } from 'pinia'
import axios from 'axios'
import snakify, { type Snakify } from 'snakify-ts'
import type { Team } from '@/types/team'
import { useStorage } from '@vueuse/core'
import camelize from 'camelize-ts'

const BASE_URL = 'http://localhost:8081/api'

export const useTeamStore = defineStore('team', {
  state: () => ({
    currentTeam: useStorage('team', null as string | null)
  }),

  getters: {
    team: (state) => state.currentTeam
  },

  actions: {
    async getTeams() {
      const teams = await axios.post(`${BASE_URL}`).then((res) => {
        if (res.status == 200) {
          // Handle the response
          return res.data
        }
      })

      return camelize(teams)
    },

    async getTeam(teamId: Number) {
      await axios.post(`${BASE_URL}/team/${teamId}/`).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async createTeam(data: Omit<Team, 'teamId'>) {
      await axios.post(`${BASE_URL}/team/`, snakify(data)).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async editTeam(data: Partial<Team>) {
      await axios.patch(`${BASE_URL}`, snakify(data)).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async joinTeam(joinCode: String) {
      await axios.post(`${BASE_URL}/users/${joinCode}`, snakify({ joinCode })).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    },

    async removeTeam(teamId: Number) {
      await axios.post(`${BASE_URL}/team/${teamId}`, snakify({ teamId })).then((res) => {
        if (res.status == 200) {
          this.currentTeam = JSON.stringify(res.data)
        }
      })
    }
  }
})
