import { defineStore } from 'pinia'
import axios from 'axios'
import snakify, { type Snakify } from 'snakify-ts'

const BASE_URL = 'http://localhost:8081/api/team'

export const useTeamStore = defineStore('team', {
  state: () => ({}),
  getters: {
    async getTeamId() {}
  },
  actions: {
    async createTeam(name: String, code: String) {
      await axios
        .post(`${BASE_URL}`, {
          name: name,
          join_code: code
        })
        .then((res) => {
          if (res.status == 200) {
            console.log()
          }
        })
    },
    async editTeam() {},
    async joinTeam() {},
    async removeTeam() {}
  }
})
