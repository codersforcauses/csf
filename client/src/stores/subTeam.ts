import { defineStore } from 'pinia'
import server from '@/utils/server'

//will get changed around later but leave as is
import { type AxiosRequestConfig } from 'axios'
import { useUserStore } from './user'

export const useSubTeamStore = defineStore('subTeam', {
  state: () => ({
    info: <any>[],
  }),
  getters: {},
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
    }
  }
})
