import { defineStore } from 'pinia'
import axios from 'axios'
import type { Event } from '../types/event'

const baseURL = 'http://localhost:8081/api/event'

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

export const useEventStore = defineStore('event', {
  state: () => ({
    events: <Event[]>[]
  }),
  actions: {
    async createEvent({isPublic = false, isArchived = false, ...partialEvent}: Event) {
      await axios
        .post(`${baseURL}/create/`, await convertKeysToCamelCase({isPublic, isArchived, ...partialEvent}))
        .then(console.log)
        .catch(console.log)
    },
    async editEvent(event: Event) {
      event = await convertKeysToCamelCase(event)

      await axios.put(`${baseURL}/update/${event.eventId}`, event)

      const i = this.events.findIndex(e => e.eventId == event.eventId)
      this.events[i] = event
    },
    async deleteEvent(eventId: number) {
      if (!this.events.find(e => eventId == e.eventId)?.isPublic) {
        await axios.delete(`${baseURL}/delete/${eventId}`)
        console.log('event deleted')
      }
    },
    async getEvents() {
      this.events = <Event[]>[]
      let { data } = await axios.get(`${baseURL}/get/`)
      this.events = await Promise.all(<Event[]>data.map(convertKeysToCamelCase))
    },
    async archiveEvent(eventId: number) {
      const event = this.events.find(e => eventId == e.eventId)
      if (event) {
        await this.editEvent({...event, isArchived: true})
        event.isArchived = true
      }
    }
  },
  getters: {}
})
