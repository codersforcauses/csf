export interface Subteam {
  subteamId: number
  name: string
  teamId: number
}

export interface MemberView {
  id: number
  firstname: string
  lastname: string
  avatar: string
}

//TODO SUBTEAM
export interface SubteamView {
  teamName: string
  teamId: string
  subteamId: string
  totalKM: string
  members: MemberView[]
}

//user
//get all subteam members: teamid, subteamid -> userids -> userlist
//get all available users: teamid -> userids (users without subteamid) -> userlist -> available users
//get all users assigned with a team: teamid -> userids (users with subteamid) -> userlist -> notAvailable users

//change user subteamid
//userid -> change subteamid

// teamid -> userids -> userlist -> available users -> noteam users
// teamid -> subteamid -> subteaminformation -> subteam
