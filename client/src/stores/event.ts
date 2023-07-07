import { defineStore } from 'pinia'
import axios, { type AxiosResponse } from 'axios'
import type { Event } from '../types/event'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'

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
    async createEvent(partialEvent: Omit<Event, 'eventId' | 'isArchived' | 'teamId'>) {
      const { data, status }: AxiosResponse<Snakify<Event>> = await axios.post(
        `${baseURL}/create/`,
        snakify({
          ...partialEvent,
          isArchived: false,
          teamId: null // temp
        })
      )
      if (status == 200) this.events.push(camelize(data))
    },
    async editEvent(event: Event) {
      const index = this.events.findIndex((e) => e.eventId == event.eventId && !e.isPublic)

      if (index > -1) {
        const { status } = await axios.put(`${baseURL}/update/${event.eventId}`, snakify(event))
        if (status == 200) this.events[index] = event
      }
    },
    async deleteEvent(eventId: Event['eventId']) {
      const index = this.events.findIndex((e) => eventId == e.eventId && !e.isPublic)

      if (index > -1) {
        const { status } = await axios.delete(`${baseURL}/delete/${eventId}`)
        if (status == 200) this.events.splice(index, 1)
      }
    },
    async getEvents() {
      const { data, status }: AxiosResponse<Snakify<Event>[]> = await axios.get(`${baseURL}/get/`)
      if (status == 200) this.events = camelize(data)
    }
  },
  getters: {}
})
