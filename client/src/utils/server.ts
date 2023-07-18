import axios, { type AxiosRequestConfig } from 'axios'
import { type Tokens } from '../types/user'

const user = JSON.parse(<string>localStorage.getItem('authToken')) as Tokens
let headers: AxiosRequestConfig['headers'] = {};

if (user?.access) {
  headers = {
    Authorization: 'Bearer ' + user?.access
  }
} else {
    headers = {}
}

export default axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL, headers })
