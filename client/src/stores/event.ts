import { defineStore } from 'pinia'
import type { Event } from '../types/event'
import camelize from 'camelize-ts'
import snakify, { type Snakify } from 'snakify-ts'
import server from '@/utils/server'
import { useUserStore } from './user'

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
        teamId: userStore.user?.teamId
      })
      const { data, status } = await server.post('event/create/', modifiedData)
      if (status == 200) this.events.push(camelize(data as Snakify<Event>))
    },
    async editEvent(event: Event) {
      const index = this.events.findIndex((e) => e.eventId == event.eventId && !e.isPublic)
      if (index > -1) {
        const { status } = await server.put(`event/update/${event.eventId}`, snakify(event))
        if (status == 200) {
          if (event.isArchived) {
            this.events.splice(index, 1)
          } else {
            this.events[index] = event
          }
        }
      }
    },
    async deleteEvent(eventId: Event['eventId']) {
      const index = this.events.findIndex((e) => eventId == e.eventId && !e.isPublic)

      if (index > -1) {
        const { status } = await server.delete(`event/delete/${eventId}`)
        if (status == 200) this.events.splice(index, 1)
      }
    },
    async getEvents() {
      const { data, status } = await server.get('event/get/')

      if (status == 200) this.events = camelize(data as Snakify<Event>[])
    }
  },
  getters: {}
})
