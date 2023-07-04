import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
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
    }
  ]
})

export default router
