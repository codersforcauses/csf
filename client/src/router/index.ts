import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import EventsView from '../views/EventsView.vue'
import ChallengeView from '../views/ChallengeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    },
    {
      path: '/challenge',
      name: 'challenge',
      component: ChallengeView
    }
  ]
})

export default router
