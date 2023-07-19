import { defineStore } from 'pinia'
import snakify from 'snakify-ts'
import type { Team } from '@/types/team'
import { useStorage } from '@vueuse/core'
import camelize from 'camelize-ts'
import type { User } from '@/types/user'
import server from '@/utils/server'
import { useUserStore } from './user'

export const useTeamStore = defineStore('team', () => {
  const userStore = useUserStore()
  const team = useStorage('team', null as Team | null)

  const removeTeamFromState = () => {
    userStore.user!.teamId = undefined
    userStore.user!.teamAdmin = false
    team.value = null
  }

  return {
    team,

    async getTeams() {
      const teams = await server.get('team/get_teams/').then((res) => {
        if (res.status == 200) {
          return res.data
        }
      })

      return camelize(teams)
    },

    async getTeam(teamId: Number) {
      const res = await server.get(`team/get/${teamId}/`)
      if (res.status == 200) team.value = camelize<Team>(res.data)
    },

    async createTeam(data: Omit<Team, 'teamId' | 'joinCode'>) {
      const res = await server.post('team/create/', snakify(data))
      if (res.status == 200) {
        team.value = camelize<Team>(res.data)
        this.joinTeam(userStore.user!.id, team.value.joinCode, true)
      }
    },

    async editTeam(data: Partial<Team>) {
      const res = await server.put(`team/edit/${team.value!.teamId}/`, snakify(data))
      if (res.status == 200) team.value = camelize<Team>(res.data)
    },

    async joinTeam(userId: number, joinCode: string, teamAdmin: boolean = false) {
      const res = await server.patch(
        `user/join/${userId}/`,
        snakify({
          joinCode,
          teamAdmin
        })
      )
      if (res.status == 200) {
        const data = camelize<Required<Pick<User, 'teamId' | 'teamAdmin'>>>(res.data)
        userStore.user!.teamId = data.teamId
        userStore.user!.teamAdmin = data.teamAdmin
        this.getTeam(data.teamId)
      }
    },

    async deleteTeam() {
      const res = await server.delete(`team/delete/${team.value!.teamId}/`)
      if (res.status == 200) removeTeamFromState()
    },

    async removeTeam() {
      const res = await server.patch(`user/remove/${userStore.user!.id}/`)
      if (res.status == 200) removeTeamFromState()
    }
  }
})
