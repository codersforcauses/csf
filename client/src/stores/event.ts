import { defineStore } from 'pinia'
import axios, {AxiosResponse} from 'axios'
import type { Event } from '../types/event'
import camelize from "camelize-ts"
import snakify, { Snakify } from "snakify-ts"

const baseURL = 'http://localhost:8081/api/event'

export const useEventStore = defineStore('event', {
  state: () => ({
    events: <Event[]>[]
  }),
  actions: {
    async createEvent(partialEvent: Omit<Event, "eventId" | "isArchived" | "teamId">) {
      const { data, status }: AxiosResponse<Snakify<Event>> = await axios
        .post(`${baseURL}/create/`, snakify({
          ...partialEvent,
          isArchived: false,
          teamId: null // temp
        }))
      if (status == 200) this.events.push(camelize(data))
    },
    async editEvent(event: Event) {
      const index = this.events.findIndex(e => e.eventId == event.eventId && !e.isPublic)

      if (index > -1) {
        await axios.put(`${baseURL}/update/${event.eventId}`, snakify(event))
        console.log("event updated")
        this.events[index] = event
      }
    },
    async deleteEvent(eventId: Event["eventId"]) {
      const index = this.events.findIndex(e => eventId == e.eventId && !e.isPublic)

      if (index > -1) {
        await axios.delete(`${baseURL}/delete/${eventId}`)
        console.log('event deleted')
        this.events.splice(index, 1)
      }
    },
    async getEvents() {
      const { data }: AxiosResponse<Snakify<Event>[]> = await axios.get(`${baseURL}/get/`)
      this.events = camelize(data)
    }
  },
  getters: {}
})
