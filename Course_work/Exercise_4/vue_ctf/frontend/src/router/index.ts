import { isTokenValid } from '@/utils/tokenUtil';
import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue';
import HomeView from '@/views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true },
    },
    {
      path: '/admin',
      name: 'admin',
      component: HomeView,
      meta: { requiresAuth: true },
    }
  ],
})

router.beforeEach((to, from, next) => {
  console.log('Navigating to:', to.fullPath);
  if (!isTokenValid()) {
    console.log('User is not authenticated, redirecting to login');
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
