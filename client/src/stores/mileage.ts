import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type Mileage from '@/types/mileage'
import camelize from 'camelize-ts'
import { notify } from '@kyvg/vue3-notification'
import { useUserStore } from './user'

export const useMileageStore = defineStore('mileage', {
  state: () => ({
    byUser: useStorage('mileageByUser', { mileage: [] as Mileage[], totalKm: 0 }),
    byTeam: useStorage('mileageByTeam', { mileage: [] as Mileage[], totalKm: 0 })
  }),
  getters: {
    mileageByUser: (state) => state.byUser.mileage,
    mileageByTeam: (state) => state.byTeam.mileage,
    totalKmByUser: (state) => state.byUser.totalKm,
    totalKmByTeam: (state) => state.byTeam.totalKm
  },
  actions: {
    addMileage(mileage: Omit<Mileage, 'mileageId'>) {
      return server
        .post('mileage/post_mileage', mileage)
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
      const user = useUserStore().user!.id
      let res = await server.get(`mileage/get_mileage`, { params: { user } })
      if (res.status == 200) this.byUser.mileage = camelize(res.data) as Mileage[]
      res = await server.get(`mileage/get_mileage`, { params: { sum: true, user } })
      if (res.status == 200) this.byUser.totalKm = res.data
    },
    async getMileageByTeam() {
      const team = useUserStore().user!.teamId
      let res = await server.get(`mileage/get_mileage`, { params: { team } })
      if (res.status == 200) this.byTeam.mileage = camelize(res.data) as Mileage[]
      res = await server.get(`mileage/get_mileage`, { params: { sum: true, team } })
      if (res.status == 200) this.byTeam.totalKm = res.data
    }
  }
})
