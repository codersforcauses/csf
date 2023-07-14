import { defineStore } from 'pinia'
import type { Event } from '../types/event'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'
import server from '@/utils/server'
import { useUserStore } from './user'
import { type AxiosRequestConfig } from 'axios'

export const useEventStore = defineStore('event', {
  state: () => ({
    events: <Event[]>[]
  }),
  actions: {
    async createEvent(partialEvent: Omit<Event, 'eventId' | 'isArchived' | 'teamId'>) {
      const userStore = useUserStore()
      const modifiedData = snakify({
        ...partialEvent,
        isArchived: false,
        teamId: null // temp
      })
      const headers: AxiosRequestConfig['headers'] = {
          Authorization: 'Bearer ' + userStore.token?.access
      }
      
      const { data, status } = await server.post('event/create/', modifiedData, headers)
      if (status == 200) this.events.push(camelize(data as Snakify<Event>))
    },
    async editEvent(event: Event) {
      const userStore = useUserStore()

      const index = this.events.findIndex((e) => e.eventId == event.eventId && !e.isPublic)
      const headers: AxiosRequestConfig['headers']  = {
        Authorization: 'Bearer ' + userStore.token?.access
      }
      if (index > -1) {
        const { status } = await server.put(`event/update/${event.eventId}`, snakify(event), headers)
        if (status == 200) this.events[index] = event
      }
    },
    async deleteEvent(eventId: Event['eventId']) {
      const userStore = useUserStore()

      const headers: AxiosRequestConfig['headers']  = {
        Authorization: 'Bearer ' + userStore.token?.access
      }

      const index = this.events.findIndex((e) => eventId == e.eventId && !e.isPublic)

      if (index > -1) {
        const { status } = await server.delete(`event/delete/${eventId}`, headers)
        if (status == 200) this.events.splice(index, 1)
      }
    },
    async getEvents() {
      const userStore = useUserStore()

      const headers: AxiosRequestConfig['headers'] = {
        Authorization: 'Bearer ' + userStore.token?.access
      }
      
      const { data, status } = await server.get('event/get/', headers)

      if (status == 200) this.events = camelize(data as Snakify<Event>[])
    }
  },
  getters: {}
})
