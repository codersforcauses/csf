import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChallengeView from '../views/ChallengeView.vue'
import { useModalStateStore } from '@/stores/openModal'

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
    }
  ]
})

router.beforeEach(async (to, from) => {
  const userStore = useUserStore()
  const modalStateStore = useModalStateStore()
  
  if (to.path == '/teams' || to.path == '/dashboard') {
    if (userStore.user == null) { 
      modalStateStore.switchState()
      // Cancel navigation if not logged in
      return false
    }
  }
})

export default router
