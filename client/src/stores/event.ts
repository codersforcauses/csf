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

      await axios
        .post(`${baseURL}/create/`, event)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async editEvent(
      eventId: number,
      name: string,
      startDate: string,
      endDate: string,
      description: string,
      isPublic: boolean,
      isArchived: boolean
    ) {
      // change it so it changes the this.event as well
      let event = {
        id: eventId,
        name: name,
        startDate: startDate,
        endDate: endDate,
        description: description,
        isPublic: isPublic,
        isArchived: isArchived
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

      await axios.put(`${baseURL}/update/${event.id}`, event)
    },
    async deleteEvent(eventId: number) {
      // event must be private
      console.log(eventId)

      await axios.delete(`${baseURL}/delete/${eventId}`).then((res) => {
        console.log('event deleted')
      })
    },
    async getEvents() {
      this.events = <Event[]>[]
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
