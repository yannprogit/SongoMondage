import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '../views/ConnexionView.vue'
import SondageListView from '../views/SondageListView.vue'
import SondageDetailsView from '../views/SondageDetailsView.vue'

const isAuthenticated = () => {
  return !!localStorage.getItem('token');
};

const routes = [
  {
    path: '/',
    name: 'sondages',
    component: SondageListView,
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
    name: 'sondage-details',
    component: SondageDetailsView,
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
