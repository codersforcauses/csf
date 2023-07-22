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
  editUserSubteam: (userId: number) => `subteam/edit_user/${userId}`
}

export const useSubTeamStore = defineStore('subTeam', {
  state: () => ({
    info: <any>[],
    subteams: [] as Subteam[],
    teamMembers: [] as UserView[],
    availableMemberList: [] as UserView[],
    subteamMembers: [] as UserView[],
    subteamsView: [] as SubteamView[]
  }),

  getters: {},

  actions: {
    // keep this optional for now as to silence warning in teampagesview.vue
    async getSubUsers() {
      const userStore = useUserStore()
      if (userStore.user && userStore.token) {
        if (userStore.token.access != null) {
          // to see what keys the user object has
          console.log(userStore.user)

          const { data } = await server.get(`subteam/get_users/${userStore.user?.teamId}`)

          console.log(data)
          this.info.push(data)
        }
      }
    },
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
        this.subteams = camelize(data as Snakify<Subteam>[]);
      }
   },
   async updateSubteams(teamId: number) {
    const api = urls.getSubteams(teamId);
    const { data, status } = await server.get(api);
    if (status === 200) {
        this.subteams = camelize(data as Snakify<Subteam>[]);
    }
    },
    async getAvailableMembers() {
        const api = urls.getAvailableMembers();
        const { data, status } = await server.get(api);
        if (status === 200) {
            this.availableMemberList = camelize(data as Snakify<UserView>[]) ;
        }
    }, 
    async getSubteamMembers(subteamId: number) {
      
      const api = urls.getSubteamMembers(subteamId)
      console.log("hello" + api)
      const { data, status } = await server.get(api)
      if (status === 200) {
        console.log("subteam members: " + JSON.stringify(data))
        this.subteamMembers = camelize(data as Snakify<UserView>[]);
        
        // console.log("subteam members: " + this.subteamMembers[0])
      }
    },
    async editUserSubteam(userId: number) {
        const api = urls.editUserSubteam(userId);
        const { data, status } = await server.put(api);
        if (status === 200) {
            this.subteamMembers = camelize(data as Snakify<UserView>[]);
        }
    },
    //get all the subteams and their members
    async getSubteamsView(teamId: number) {
      this.subteamsView = []

      let membersView: MemberView[] = []
      const totalKm = 0

     await this.getSubteams(teamId)
      console.log("subteams loaded")

      this.subteams.forEach(async (subteam) => {
        //convert from user type to memberview type
        console.log("subteam: " + subteam.subteamId)
        await  this.getSubteamMembers(subteam.subteamId)
        console.log("subteam members loaded")

        membersView = this.subteamMembers.map((member) => {
            return {
              id: member.id,
              firstName: member.firstName,
              lastName: member.lastName,
              avatar: member.avatar
            }
          });
        
        const data = snakify({
          ...subteam,
          totalKm: totalKm.toString() + 'KM',
          members: membersView          
        })
        this.subteamsView.push(camelize(data as Snakify<SubteamView>))
      });
      console.log("subteams view loaded")
    },    
  }
})
