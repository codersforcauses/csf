import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type Mileage from '@/types/mileage'
import camelize from 'camelize-ts'
import { notify } from '@kyvg/vue3-notification'

export const useMileageStore = defineStore('mileage', {
  state: () => ({
    recentMileage: useStorage('recentMileage', [] as Mileage[])
  }),
  actions: {
    async postMileage(userId: number, kilometres: number, date: string) {
      await server
        .post('mileage/post_mileage/', {
          user: userId,
          kilometres: kilometres,
          date: date
        })
        .then(async () => {
          await this.getRecentMileage(userId)
        })
        .finally(() => {
          notify({
            title: 'Post Mileage',
            type: 'success',
            text: 'Post Mileage Successful'
          })
        })
        .catch(() => {
          notify({
            title: 'Post Mileage',
            type: 'error',
            text: 'Post Mileage Error'
          })
        })
    },

    async getRecentMileage(userId: number) {
      await server
        .get(`mileage/get_mileage/${userId}`, {
          params: {
            challenge: true
          }
        })
        .then((res) => {
          if (res.status == 200) {
            this.recentMileage = camelize(res.data) as Mileage[]
          }
        })
    }
  }
})
