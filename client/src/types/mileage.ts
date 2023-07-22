export default interface Mileage {
  mileageId: number
  userId: number
  kilometres: number
  date: string
}

export interface GetLeaderboardParam {
  type: 'users' | 'teams'
  username?: string
  teamName?: string
}

export interface UserLeaderboard {
  leaderboard: RankedUserLeaderboardEntry[]
  user?: RankedUserLeaderboardEntry
}

export interface TeamLeaderboard {
  leaderboard: RankedTeamLeaderboardEntry[]
  team?: RankedTeamLeaderboardEntry
}

export interface RankedUserLeaderboardEntry {
  username: string
  totalMileage: number
  rank: number
}

export interface RankedTeamLeaderboardEntry {
  name: string
  bio: string
  totalMileage: number
  rank: number
}
