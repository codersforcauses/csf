import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type Mileage from '@/types/mileage'
import camelize from 'camelize-ts'
import { notify } from '@kyvg/vue3-notification'
import { useUserStore } from './user'

export const useMileageStore = defineStore('mileage', {
  state: () => ({
    mileageByUser: useStorage('mileageByUser', [] as Mileage[]),
    mileageByTeam: useStorage('mileageByTeam', [] as Mileage[])
  }),
  getters: {
    totalKmByUser: (state) => state.mileageByUser.reduce((acc, cur) => acc + cur.kilometres, 0),
    totalKmByTeam: (state) => state.mileageByTeam.reduce((acc, cur) => acc + cur.kilometres, 0)
  },
  actions: {
    addMileage(mileage: Omit<Mileage, 'mileageId'>) {
      return server
        .post('mileage/post_mileage/', mileage)
        .then(async () => {
          await this.getMileageByUser()
          await this.getMileageByTeam()
          notify({
            title: 'Post Mileage',
            type: 'success',
            text: 'Post Mileage Successful'
          })
        })
        .catch(() =>
          notify({
            title: 'Post Mileage',
            type: 'error',
            text: 'Post Mileage Error'
          })
        )
    },
    async getMileageByUser() {
      const { status, data } = await server.get(
        `mileage/get_mileage/user/${useUserStore().user!.id}`,
        { params: { challenge: true } }
      )
      if (status == 200) this.mileageByUser = <Mileage[]>camelize(data)
    },
    async getMileageByTeam() {
      const { status, data } = await server.get(
        `mileage/get_mileage/team/${useUserStore().user!.teamId!}`,
        { params: { challenge: true } }
      )
      if (status == 200) this.mileageByTeam = camelize(data) as Mileage[]
    }
  }
})
