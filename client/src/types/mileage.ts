export default interface Mileage {
  mileageId: number
  userId: number
  kilometres: number
  date: string
}

export interface UserLeaderboardEntry {
  username: string
  totalMileage: number
}

export interface RankedUserLeaderboardEntry {
  username: string
  totalMileage: number
  rank: number
}

export interface TeamLeaderboardEntry {
  name: string
  bio: string
  totalMileage: number
}

export interface RankedTeamLeaderboardEntry {
  name: string
  bio: string
  totalMileage: number
  rank: number
}