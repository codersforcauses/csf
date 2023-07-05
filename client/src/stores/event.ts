import { defineStore } from 'pinia'
import axios from 'axios'

const baseURL = 'http://localhost:8081/api/event'

export const useEventStore = defineStore('event', {
  state: () => ({
    events: <Event[]>[]
  }),
  actions: {
    async createEvent(name: string, startDate: string, endDate: string, description: string) {
      let event = {
        name: name,
        startDate: startDate,
        endDate: endDate,
        description: description,
        isPublic: false,
        isArchived: false
      }

      const convertKeysToCamelCase = <T>(obj: { [key: string]: any }): T => {
        const newObj: { [key: string]: any } = {}
        for (const key in obj) {
          // eslint-disable-next-line no-prototype-builtins
          if (obj.hasOwnProperty(key)) {
            const snakeCaseKey = key.replace(/([a-z])([A-Z])/g, '$1_$2').toLowerCase()
            newObj[snakeCaseKey] = obj[key]
          }
        }
        return newObj as T
      }

      event = await convertKeysToCamelCase(event)
      console.log(event)

      await axios
        .post(`${baseURL}/create/`, event)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async editEvent(event: Event) {
      // event must be private
    },
    async archiveEvent(event: Event) {
      //set archived to true
    },
    async deleteEvent(event: Event) {
      // event must be private
    },
    async getEvents() {
      let events = <Event[]>[]
      await axios.get<Event[]>(`${baseURL}/get/`).then((result) => {
        events = result.data
      })

      const convertKeysToCamelCase = <T>(obj: { [key: string]: any }): T => {
        const newObj: { [key: string]: any } = {}
        for (const key in obj) {
          // eslint-disable-next-line no-prototype-builtins
          if (obj.hasOwnProperty(key)) {
            const camelCaseKey = key.replace(/_(\w)/g, (_, p1) => p1.toUpperCase())
            newObj[camelCaseKey] = obj[key]
          }
        }
        return newObj as T
      }

      for (let i = 0; i < events.length; i++) {
        events[i] = await convertKeysToCamelCase(events[i])
      }
      this.events = [...events]
    }
  },
  getters: {}
})
