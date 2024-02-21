export default interface Mileage {
  mileageId: number
  user: number
  kilometres: number
  date: string
}

export interface GetLeaderboardParam {
  type: 'users' | 'teams' | 'team'
  userId?: number
  teamId?: number
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
  teamId: number
}

export interface RankedTeamLeaderboardEntry {
  name: string
  bio: string
  totalMileage: number
  rank: number
}
