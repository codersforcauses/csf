export interface Subteam {
  subteamId: number
  name: string
  teamId: number
}

export interface MemberView {
  id: number
  firstName: string
  lastName: string
  avatar: string
}

export interface SubteamView {
  subteamId: number
  name: string
  teamId: number
  totalKm: string
  members: MemberView[]
}

export interface UserView {
  id: number
  username: string
  firstName: string
  lastName: string
  email: string
  subteamId: number
  teamId: number
  avatar: string
  teamAdmin: boolean
}
