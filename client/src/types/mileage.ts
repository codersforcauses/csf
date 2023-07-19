export default interface Mileage {
  mileageId: number
  userId: number
  kilometres: number
  date: string
}

export interface GetLeaderboardParam {
  type: "users" | "teams"
  username?: string
  teamName?: string
}

export interface UserLeaderboard {
  leaderboard: UserLeaderboardEntry[]
  user?: RankedUserLeaderboardEntry
}

export interface TeamLeaderboard {
  leaderboard: TeamLeaderboardEntry[]
  team?: RankedTeamLeaderboardEntry
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