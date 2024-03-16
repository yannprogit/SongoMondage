import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '../views/ConnexionView.vue'
import SondagesListView from '../views/SondagesListView.vue'
import SondageView from '../views/SondageView.vue'
import MesSondagesListView from '../views/MesSondagesListView.vue'

const isAuthenticated = () => {
  return !!localStorage.getItem('token');
};

const routes = [
  {
    path: '/',
    name: 'sondages',
    component: SondagesListView,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next();
      } else {
        next('/connexion');
      }
    }
  },
  {
    path: '/mes_sondages',
    name: 'mes_sondages',
    component: MesSondagesListView,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next();
      } else {
        next('/connexion');
      }
    }
  },
  {
    path: '/connexion',
    name: 'connexion',
    component: ConnexionView,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next('/');
      } else {
        next();
      }
    }
  },
  {
    path: '/sondages/:id',
    name: 'sondage',
    component: SondageView,
    props: true, 
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next();
      } else {
        next('/connexion');
      }
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
