import { createRouter, createWebHistory } from 'vue-router'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import MileageModalView from '../views/MileageModalView.vue'

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
      path: '/mileagemodal',
      name: 'mileagemodal',
      component: MileageModalView
    }
  ]
})

export default router
