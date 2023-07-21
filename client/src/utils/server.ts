import { useUserStore } from '@/stores/user'
import axios, { AxiosError } from 'axios'

// @ts-ignore 2339
const server = axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL })

server.interceptors.request.use((config) => {
  const userStore = useUserStore()
  if (userStore.token != null)
    config.headers = { ...config.headers, Authorization: 'Bearer ' + userStore.token.access }
  return config
})

server.interceptors.response.use(
  (r) => r,
  async (error: AxiosError & { config: { token_refreshed?: boolean } }) => {
    if (error.response?.status == 401 && !error.config?.token_refreshed) {
      error.config.token_refreshed = true
      if (await useUserStore().refreshToken()) return server(error.config)
    }
    return Promise.reject(error)
  }
)

export default server
