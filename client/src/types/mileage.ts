export interface Mileage {
  mileageId: number
  userId: number
  kilometres: number
  date: string
}

export interface UserLeaderboardEntry {
  username: string
  totalMileage: number
}