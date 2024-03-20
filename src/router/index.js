import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '../views/ConnexionView.vue'
import SondagesListView from '../views/SondagesListView.vue'
import SondageView from '../views/SondageView.vue'
import MesSondagesListView from '../views/MesSondagesListView.vue'
import AddSondageView from '../views/AddSondageView.vue'
import ReponseView from '../views/ReponseView.vue'
import ReponsesListView from '../views/ReponsesListView.vue'

const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  let ok = false;
  if (token) {
    ok = true;
  }
  return ok;
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
    path: '/mes-sondages',
    name: 'mes-sondages',
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
    path: '/ajout-sondage',
    name: 'ajout-sondage',
    component: AddSondageView,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next();
      } else {
        next('/connexion');
      }
    }
  },
  {
    path: '/sondages/:id/reponses',
    name: 'reponses',
    component: ReponsesListView,
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
    path: '/sondages/:sondage_id/reponses/:id',
    name: 'reponse',
    component: ReponseView,
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
