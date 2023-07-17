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

export interface UserSettings {
  username: string
  firstName: string
  lastName: string
  email: string
  avatar: string
  travelMethod: string
}

export interface ChangeDetailsError {
  username?: string | string[]
  email?: string | string[]
  firstName?: string | string[]
  lastName?: string | string[]
}

export interface ChangePasswordError {
  oldPassword?: string
  password?: string
}
