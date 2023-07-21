import { defineStore } from 'pinia'
import snakify from 'snakify-ts'
import type { Team } from '@/types/team'
import camelize from 'camelize-ts'
import type { User } from '@/types/user'
import server from '@/utils/server'
import { notify } from '@kyvg/vue3-notification'
import { useUserStore } from './user'
import useNullableStorage from '@/utils/useNullableStorage'

export const useTeamStore = defineStore('team', () => {
  const userStore = useUserStore()
  const team = useNullableStorage<Team>('team')

  const removeTeamFromState = () => {
    userStore.user!.teamId = undefined
    userStore.user!.teamAdmin = false
    team.value = null
  }

  return {
    team,

    async getTeams() {
      const teams = await server.get('team/get_teams/').then((res) => {
        if (res.status == 200) return res.data
      })
      notify({
        title: 'Get Teams',
        type: 'error',
        text: 'Get Teams Error'
      })
      return camelize(teams)
    },

    async getTeam(teamId: Number) {
      const res = await server.get(`team/get/${teamId}/`)
      if (res.status == 200) team.value = camelize<Team>(res.data)
      else
        notify({
          title: 'Get Team',
          type: 'error',
          text: 'Get Team Error'
        })
    },

    async createTeam(data: Omit<Team, 'teamId' | 'joinCode'>) {
      const res = await server.post('team/create/', snakify(data))
      if (res.status == 200) {
        team.value = camelize<Team>(res.data)
        this.joinTeam(team.value.joinCode, true)
        notify({
          title: 'Create Team',
          type: 'success',
          text: 'Create Team Successful'
        })
      } else {
        notify({
          title: 'Create Team',
          type: 'error',
          text: 'Create Team Error'
        })
      }
    },

    async editTeam(data: Partial<Team>) {
      const res = await server.put(`team/edit/${team.value!.teamId}/`, snakify(data))
      if (res.status == 200) {
        notify({
          title: 'Edit Team',
          type: 'success',
          text: 'Edit Team Successful'
        })
        team.value = camelize<Team>(res.data)
      } else {
        notify({
          title: 'Edit Team',
          type: 'error',
          text: 'Edit Team Error'
        })
      }
    },

    async joinTeam(joinCode: string, teamAdmin: boolean = false) {
      const res = await server.patch(
        `user/join/${userStore.user!.id}/`,
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
        notify({
          title: 'Join Team',
          type: 'success',
          text: 'Join Team Successful'
        })
      } else if (res.status == 404) {
        notify({
          title: 'Join Team',
          type: 'error',
          text: 'Team Does Not Exists'
        })
      } else {
        notify({
          title: 'Join Team',
          type: 'error',
          text: 'Join Team Error'
        })
      }
    },

    async deleteTeam() {
      const res = await server.delete(`team/delete/${team.value!.teamId}/`)
      if (res.status == 200) {
        removeTeamFromState()
        notify({
          title: 'Delete Team',
          type: 'success',
          text: 'Delete Team Successful'
        })
      } else {
        notify({
          title: 'Delete Team',
          type: 'error',
          text: 'Delete Team Error'
        })
      }
    },

    async removeTeam() {
      const res = await server.patch(`user/remove/${userStore.user!.id}/`)
      if (res.status == 200) {
        removeTeamFromState()
        notify({
          title: 'Remove Team',
          type: 'success',
          text: 'Remove Team Successful'
        })
      } else {
        notify({
          title: 'Remove Team',
          type: 'error',
          text: 'Remove Team Error'
        })
      }
    }
  }
})
