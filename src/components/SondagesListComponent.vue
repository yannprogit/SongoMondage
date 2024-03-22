<template>
      <div class="object_item" v-for="sondage in sondages" :key="sondage._id">
        <router-link :to="{ name: 'sondage', params: { id: sondage._id } }">
        <h3>{{ sondage.nom }}</h3>
        <p v-if="isCreateur(sondage.createur)">Créateur: Moi</p>
        <p v-else-if="utilExist(sondage.createur)">Créateur: {{ getNom(sondage.createur) }}</p>
        <p v-else>Créateur: Inconnu</p>
        <p>Nombre de questions: {{ sondage.questions.length }}</p>
        </router-link>
      </div>
      <notification :message="notificationMessage" :urlPage="urlPageNotification" v-if="showNotification" @notificationClosed="showNotification = false"/>
</template>
  
  <script>
  import axios from 'axios';
  import VueJwtDecode from 'vue-jwt-decode';
  import Notification from './NotificationComponent.vue';

  export default {
    props: {
        sondages: {
            type: Array,
            required: true
        }
    },
    components: {
      Notification
    },
    data() {
      return {
        utils: [],
        showNotification: false,
        notificationMessage: '',
        urlPageNotification: null
      };
    },
    mounted() {
      const token = localStorage.getItem('token');

        if (token) {
            axios.get('http://127.0.0.1:8080/utilisateurs/names', {
            headers: {
                'Authorization': `${token}`
            }
            })
            .then(response => {
            this.utils = response.data.utils;
            })
            .catch(() => {
              this.showNotification = true;
              this.notificationMessage = "Une erreur s'est produite";
              this.urlPageNotification = '/';
            });
        } else {
          this.$router.push('/connexion');
        }
    },
    methods: {
      isCreateur(id) {
        const token = localStorage.getItem('token');
        if (token) {
          const decodedToken = VueJwtDecode.decode(token);
          return id == decodedToken.id;
        } else {
          this.$router.push('/connexion');
        }
      },
      getNom(id) {
        for (const util of this.utils) {
          if (util._id == id) {
            return util.nom;
          }
        }
        return null;
      },
      utilExist(id) {
        return this.utils.some(util => util._id == id);
      }
    }
  };
  </script>
  