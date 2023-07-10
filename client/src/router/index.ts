import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import DashboardView from '../views/DashboardView.vue'
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
  if (to.path == '/teams' || to.path == '/dashboard') {
    if (userStore.user == null) { 
      // Cancel navigation if not logged in
      return false
    }
  }
})

router.afterEach((to, from, failure) => {
  if (failure) {
    // Run event if not logged in
    console.log("not logged in")
    // This is where I will make it open login modal
  }
})

export default router
