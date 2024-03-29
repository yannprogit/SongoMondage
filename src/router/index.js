import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '../views/ConnexionView.vue'
import SondagesListView from '../views/SondagesListView.vue'
import SondageView from '../views/SondageView.vue'
import MesSondagesListView from '../views/MesSondagesListView.vue'
import AddSondageView from '../views/AddSondageView.vue'
import UpdSondageView from '../views/UpdSondageView.vue'
import ReponseView from '../views/ReponseView.vue'
import ReponsesListView from '../views/ReponsesListView.vue'
import AccueilView from '../views/AccueilView.vue'
import InscriptionView from '../views/InscriptionView.vue'

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
    name: 'accueil',
    component: AccueilView,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next();
      } else {
        next('/connexion');
      }
    }
  },
  {
    path: '/sondages',
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
    path: '/inscription',
    name: 'inscription',
    component: InscriptionView,
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
    path: '/sondages/:id/modification',
    name: 'modification-sondage',
    component: UpdSondageView,
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
