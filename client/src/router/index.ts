import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import Login from '@/components/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/teams',
      name: 'teams',
      component: TeamsPageView
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signUp',
      component: SignupView
    }
  ]
})

export default router
