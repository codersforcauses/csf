import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '../views/SignupView.vue'
import EventsView from '../views/EventsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    }
  ]
})

export default router
