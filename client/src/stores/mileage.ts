import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type { Mileage } from '@/types/mileage'
import camelize from 'camelize-ts'

export const useMileageStore = defineStore('recentMileage', {
    state: () => ({
      recentMileageS: useStorage('recentMileage', '[]' as string)
    }),
    getters: {
        recentMileage: (state) => JSON.parse(state.recentMileageS) as Mileage[]
    },
    actions: {
      async getRecentMileage(userId: number) {
        await server
        .get(`mileage/get_mileage/${userId}`, {
            params: {
                challenge: true
            }
        })
        .then((res) => {
          if (res.status == 200) {
            this.recentMileageS = JSON.stringify(camelize(res.data))
          }
        })
      }
    }
  })
  