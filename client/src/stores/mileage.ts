import { defineStore } from 'pinia'
import { useStorage } from '@vueuse/core'
import server from '@/utils/server'
import type { GetLeaderboardParam, UserLeaderboard, TeamLeaderboard } from '@/types/mileage'
import type Mileage from '@/types/mileage'
import camelize from 'camelize-ts'
import snakify from 'snakify-ts'

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
    },
    async getLeaderboard(param: GetLeaderboardParam) {
      return await server.get('mileage/get_leaderboard/', {
        params: snakify(param)
      }).then((res) => {
        if (res.status == 200) {
          return camelize(res.data) as unknown as UserLeaderboard | TeamLeaderboard
        }
      })
    }
  }
})
