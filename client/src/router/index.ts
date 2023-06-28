import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import SignUpView from '../views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'about',
      component: AboutView
    },
    {
      path: '/signup',
      name: 'signUp',
      component: SignUpView
    }
  ]
})

export default router
