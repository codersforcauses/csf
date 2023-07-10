export interface User {
  id: Number
  username: string
  firstName: string
  lastName: string
  email: string
  avatar: string
  travelMethod: string
  teamSignup: boolean
  hasConsent: boolean
}

export interface Signup {
  username: string
  firstName: string
  lastName: string
  email: string
  password: string
  confirmPassword: string
  avatar: string
  travelMethod: string
  teamSignup: boolean
  hasConsent: boolean
}
