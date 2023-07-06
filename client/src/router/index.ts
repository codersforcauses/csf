import { createRouter, createWebHistory } from 'vue-router'
<<<<<<< HEAD
import AboutView from '../views/AboutView.vue'
=======
import TeamsPageView from '@/views/TeamsPageView.vue'
>>>>>>> main
import EventsView from '../views/EventsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
<<<<<<< HEAD
      path: '/',
      name: 'about',
      component: AboutView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
=======
      path: '/teams',
      name: 'teams',
      component: TeamsPageView
>>>>>>> main
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    }
  ]
})

export default router
