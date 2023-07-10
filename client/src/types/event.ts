export interface Event {
  eventId: number
  name: string
  startDate: string
  endDate: string
  description: string
  isPublic: boolean
  isArchived: boolean
  teamId: number | null
}
