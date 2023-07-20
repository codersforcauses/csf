import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import AboutView from '../views/AboutView.vue'
import TeamsPageView from '@/views/TeamsPageView.vue'
import EventsView from '../views/EventsView.vue'
import UserSettingsView from '../views/UserSettingsView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChallengeView from '../views/ChallengeView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import { capitalize } from 'vue'
import { useModalStore } from '@/stores/modal'

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
    }
    // {
    //   path: '/:pathMatch(.*)*',
    //   name: 'not-found',
    //   component: NotFoundView
    // }
  ]
})

router.beforeEach(async (to, from) => {
  const userStore = useUserStore()
  const modalStore = useModalStore()

  if (to.path == '/team' || to.path == '/dashboard') {
    if (userStore.user == null) {
      modalStore.login()
      // Cancel navigation if not logged in
      return false
    }
  }
})

router.afterEach((to, from, failure) => {
  if (!failure) {
    document.title =
      (to.path != '/' && typeof to.name == 'string' ? capitalize(to.name) + ' - ' : '') +
      'Stride For Education'
  }
})

export default router
