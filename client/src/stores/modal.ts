import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

// export const useModalStore = defineStore('modalState', {
//   state: () => ({
//     status: ,
//     username: '',
//     password: '',
//   }),
//   actions: {
//     register() {
//       this.status = 'register'
//     },
//     login() {
//       this.status = 'login'
//     },
//     close() {
//       this.status = 'closed'
//     }
//   }
// })

export const useModalStore = defineStore('modalState', () => {
  const status = ref<'closed' | 'login' | 'register'>('closed')
  const username = ref('')
  const password = ref('')

  const register = () => (status.value = 'register')
  const login = () => (status.value = 'login')
  const close = () => {
    status.value = 'closed'
    username.value = ''
    password.value = ''
  }

  const isRegister = computed({
    get: () => status.value === 'register',
    set: (v) => (v ? register() : close())
  })
  const isLogin = computed({
    get: () => status.value === 'login',
    set: (v) => (v ? login() : close())
  })
  const isOpen = computed(() => status.value !== 'closed')

  return { username, password, register, login, close, isRegister, isLogin, isOpen }
})
