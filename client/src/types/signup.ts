export interface Signup {
  username: string
  firstName: string
  lastName: string
  email: string
  password: string
  confirmPassword?: string // gonna remove before sending to server
  avatar?: string // ^^^
  travelMethod: string
  teamSignup: boolean
  hasConsent: boolean
}
