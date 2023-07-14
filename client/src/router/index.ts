import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
<<<<<<< HEAD
import DashboardView from '../views/DashboardView.vue'
=======
import UserSettingsView from '../views/UserSettingsView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChallengeView from '../views/ChallengeView.vue'
import { capitalize } from 'vue'
>>>>>>> main

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'about',
      component: AboutView
    },
    {
      path: '/team',
      name: 'team',
      component: TeamsPageView
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    },
    {
<<<<<<< HEAD
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
=======
      path: '/settings',
      name: 'settings',
      component: UserSettingsView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/challenges',
      name: 'challenges',
      component: ChallengeView
>>>>>>> main
    }
  ]
})

router.beforeEach((to, from, next) => {
  document.title =
    (to.path != '/' && typeof to.name == 'string' ? capitalize(to.name) + ' - ' : '') +
    'Stride For Education'
  next()
})

export default router
