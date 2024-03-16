import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '../views/ConnexionView.vue'
import SondageView from '../views/SondageView.vue'
import SondageDetailsView from '../views/SondageDetailsView.vue'

const isAuthenticated = () => {
  return !!localStorage.getItem('token');
};

const routes = [
  {
    path: '/',
    name: 'sondage',
    component: SondageView,
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
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
