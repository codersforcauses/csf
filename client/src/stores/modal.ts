import { defineStore } from 'pinia'
import { computed } from 'vue'

export const useModalStore = defineStore('modalState', {
  state: () => ({
    _status: 'closed' as 'closed' | 'register' | 'login',
    fields: { username: '', password: '' }
  }),
  getters: {
    isRegister: (state) => state._status === 'register',
    isLogin: (state) => state._status === 'login',
    isOpen: (state) => state._status !== 'closed',
    computedFields: (state) => ({
      username: computed({
        get: () => state.fields.username,
        set: (v) => (state.fields.username = v)
      }),
      password: computed({
        get: () => state.fields.password,
        set: (v) => (state.fields.password = v)
      })
    })
  },
  actions: {
    register() {
      this._status = 'register'
    },
    login() {
      this._status = 'login'
    },
    close() {
      this._status = 'closed'
      this.fields.username = ''
      this.fields.password = ''
    }
  }
})
