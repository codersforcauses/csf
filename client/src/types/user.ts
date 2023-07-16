export interface User {
  id: number
  username: string
  firstName: string
  lastName: string
  email: string
  avatar: string
  travelMethod: string
  teamSignup: boolean
  hasConsent: boolean
  subteamId?: number
  teamId?: number
  teamAdmin?: Boolean
}

export interface Signup {
  username: string
  firstName: string
  lastName: string
  email: string
  password: string
  confirmPassword?: string
  avatar?: string
  travelMethod: string
  teamSignup: boolean
  hasConsent: boolean
}
