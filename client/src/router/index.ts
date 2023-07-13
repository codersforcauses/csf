import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChallengeView from '../views/ChallengeView.vue'
import NotFoundView from '../views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'about',
      component: AboutView
    },
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
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/challenge',
      name: 'challenge',
      component: ChallengeView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFoundView
    }
  ]
})

export default router
