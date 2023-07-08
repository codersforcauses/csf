import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import ChallengeView from '../views/ChallengeView.vue'

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
      path: '/challenge',
      name: 'challenge',
      component: ChallengeView
    }
  ]
})

export default router
