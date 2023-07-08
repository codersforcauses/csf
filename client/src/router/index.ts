import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChallengeView from '../views/ChallengeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/teams',
      name: 'teams',
      component: TeamsPageView
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
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
  ]
})

export default router
