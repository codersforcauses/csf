import { defineStore } from 'pinia'
import server from '@/utils/server'
import type { Subteam, SubteamView, MemberView, UserView } from '@/types/subteam'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'

//will get changed around later but leave as is
import { useUserStore } from './user'

const urls = {
  createSubteam: () => `subteam/create/`,
  getSubteams: (teamId: number) => `subteam/get_subteams/${teamId}`,
  updateSubteam: (subTeamId: number) => `subteam/update_subteam/${subTeamId}`,
  deleteSubteam: (subTeamId: number) => `subteam/delete_subteam/${subTeamId}`,
  getSubteamMembers: (subTeamId: number) => `subteam/get_users/${subTeamId}`,
  getAvailableMembers: () => `subteam/get_available_users/`,
  editUserSubteam: (userId: number) => `subteam/edit_user/${userId}`,
  deleteSubteamMember: (userId: number) => `subteam/delete_user_from_subteam/${userId}`
}

export const useSubTeamStore = defineStore('subTeam', {
  state: () => ({
    subteams: [] as Subteam[],
    teamMembers: [] as UserView[],
    availableMemberList: [] as UserView[],
    subteamMembers: [] as UserView[],
    subteamsView: [] as SubteamView[]
  }),

  actions: {
    async createSubteam(partialSubteam: Omit<Subteam, 'subteamId'>) {
      const api = urls.createSubteam()
      const { data, status } = await server.post(
        api,
        snakify({
          ...partialSubteam
        })
      )
      if (status === 200) {
        this.subteams.push(camelize(data as Snakify<Subteam>))
      }
    },
    async editSubteam(subteam: Subteam) {
      const index = this.subteams.findIndex((s) => s.subteamId === subteam.subteamId)

      if (index > -1) {
        const subTeamId = subteam.subteamId
        const { status } = await server.put(urls.updateSubteam(subTeamId), snakify(subteam))
        if (status === 200) {
          this.subteams[index] = subteam
        }
      }
    },
    async deleteSubteam(subteamId: number) {
      const index = this.subteams.findIndex((s) => subteamId === s.subteamId)

      if (index > -1) {
        const { status } = await server.delete(urls.deleteSubteam(subteamId))
        if (status === 200) {
          this.subteams.splice(index, 1)
        }
      }
    },
    async getSubteams(teamId: number) {
      const api = urls.getSubteams(teamId)
      const { data, status } = await server.get(api)
      if (status === 200) {
        this.subteams = camelize(data as Snakify<Subteam>[])
      }
    },
    async updateSubteam(subteam: Subteam) {
      const subteamId = subteam.subteamId
      const api = urls.updateSubteam(subteamId)
      await server.put(api, snakify({ ...subteam }))
    },
    async getAvailableMembers() {
      const api = urls.getAvailableMembers()
      const { data, status } = await server.get(api)
      if (status === 200) {
        this.availableMemberList = camelize(data as Snakify<UserView>[])
      }
    },
    async getSubteamMembers(subteamId: number) {
      const api = urls.getSubteamMembers(subteamId)
      const { data, status } = await server.get(api)
      if (status === 200) {
        this.subteamMembers = camelize(data as Snakify<UserView>[])
      }
    },
    async editUserSubteam(subteamId: number, userId: number) {
      const api = urls.editUserSubteam(userId)
      await server.put(api, snakify({ subteamId }))
    },
    async removeSubteamMember(userId: number) {
      const api = urls.deleteSubteamMember(userId)
      await server.put(api)
    },

    //get all the subteams and their members
    async getSubteamsView(teamId: number) {
      this.subteamsView = []

      let membersView: MemberView[] = []
      const totalKm = 0

      await this.getSubteams(teamId)

      this.subteams.forEach(async (subteam) => {
        //convert from user type to memberview type
        await this.getSubteamMembers(subteam.subteamId)
        membersView = this.subteamMembers.map((member) => {
          return {
            id: member.id,
            firstName: member.firstName,
            lastName: member.lastName,
            avatar: `/src/assets/Avatars/${member.avatar}`
          }
        })

        const data = snakify({
          ...subteam,
          totalKm: totalKm.toString() + 'KM',
          members: membersView
        })
        this.subteamsView.push(camelize(data as Snakify<SubteamView>))
      })
    },
    async removeMembersFromSubteam(subteamId: number) {
      await this.getSubteamMembers(subteamId)
      this.subteamMembers.forEach(async (member) => {
        await this.removeSubteamMember(member.id)
      })
    }
  }
})
