import { defineStore } from 'pinia'
import server from '@/utils/server'

import type { Subteam, SubteamView, MemberView } from '@/types/subteam'
import type { User } from '@/types/user'

import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'

//will get changed around later but leave as is
import { type AxiosRequestConfig } from 'axios'
import { useUserStore } from './user'

const urls = {
  createSubteam: () => `create/`,
  getSubteams: (teamId: number) => `get_subteams/${teamId}`,
  updateSubteam: (subTeamId: number) => `update_subteam/${subTeamId}`,
  deleteSubteam: (subTeamId: number) => `delete_subteam/${subTeamId}`,

  getSubteamMembers: (subTeamId: number) => `get_users/${subTeamId}`,
  getAvailableMembers: () => `get_available_users/`,
  editUserSubteam: (userId: number) => `edit_user/${userId}`
};

export const useSubTeamStore = defineStore('subTeam', {
  state: () => ({
    info: <any>[],
    subteams: [] as Subteam[],
    teamMembers: [] as User[],
    avalidableMemberList: [] as User[],
    subteamMembers: [] as User[]
  }),

  getters: {
    //get all the subteams and their members
    subteamsInfo(state): SubteamView[] {
      const view: SubteamView[] = []
      let membersView: MemberView[] = []

      const totalKM = 0
      state.subteams.forEach((subteam) => {
        // const members = state.teamMembers.filter(
        //   (user) => {
        //     //filter members for each subteam
        //     if (user.subteamId){
        //       return user.subteamId == subteam.subteamId
        //     }
        //   }
        // );

      //convert from user type to memberview type
      membersView = state.subteamMembers.map((member) => {
          return {
            id: member.id,
            firstname: member.firstName,
            lastname: member.lastName,
            avatar: member.avatar
          }
        });


      view.push({
        ...subteam,
        totalKM: totalKM.toString(),
        members: membersView
      })

      });
      return view;
    },
  },

  actions: {
    async getSub() {
      console.log('hello subteams')
    },
    // keep this optional for now as to silence warning in teampagesview.vue
    async getSubUsers(subTeamId?: number) {
      const userStore = useUserStore()

      if (userStore.token.access != null) {
        const headers: AxiosRequestConfig['headers'] = {
          Authorization: 'Bearer ' + userStore.token?.access
        }
        console.log(headers);
        
        const { data } = await server.get(`subteam/get_users/${subTeamId}`, headers)

        // console.log(data, status)
        this.info.push(data)
      }
    },
    async createSubteam(partialSubteam: Omit<Subteam, 'subteamId'>) {
      const api = urls.createSubteam();
      const { data, status } = await server.post(
          api,
          snakify({
              ...partialSubteam,
          })
      );
      if (status === 200) {
          this.subteams.push(camelize(data as Snakify<Subteam>));
      }
    },
    async editSubteam(subteam: Subteam) {
      const index = this.subteams.findIndex(
          (s) => s.subteamId === subteam.subteamId
      );

      if (index > -1) {
          const subTeamId = subteam.subteamId;
          const { status } = await server.put(urls.updateSubteam(subTeamId), snakify(subteam));
          if (status === 200) {
              this.subteams[index] = subteam;
          }
      }
    },
    async deleteSubteam(subteamId: number) {
      const index = this.subteams.findIndex(
          (s) => subteamId === s.subteamId
      );

      if (index > -1) {
          const { status } = await server.delete(urls.deleteSubteam(subteamId));
          if (status === 200) {
              this.subteams.splice(index, 1);
          }
      }
   },
   async getSubteams(teamId: number) {
    const api = urls.getSubteams(teamId);
    const { data, status } = await server.get(api);
    if (status === 200) {
        this.subteams = data;
    }
    },
    async getAvailableMembers() {
        const api = urls.getAvailableMembers();
        const { data, status } = await server.get(api);
        if (status === 200) {
            this.avalidableMemberList = data;
        }
    }, 
    async getSubteamMembers(subteamId: number) {
        const api = urls.getSubteamMembers(subteamId);
        const { data, status } = await server.get(api);
        if (status === 200) {
            this.subteamMembers = data;
        }
    },
    async editUserSubteam(userId: number) {
        const api = urls.editUserSubteam(userId);
        const { data, status } = await server.put(api);
        if (status === 200) {
            this.subteamMembers = data;
        }
    }    
  }
})
