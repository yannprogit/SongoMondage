<template>
    <div class="sondage">
      <div v-if="sondages.length!=0" class="background_bubble"><h2>Mes Sondages</h2></div>
      <div v-else class="background_bubble">
        <p>Vous n'avez aucun sondage, cliquez sur</p>
        <p>ajouter pour en créer un !</p>
      </div>
      <router-link to="/ajout-sondage">
        <button>Ajouter</button>
      </router-link>
      <SondagesListComponent :sondages="sondages" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SondagesListComponent from '@/components/SondagesListComponent.vue';
  
  export default {
    name: 'SondageListView',
    components: {
      SondagesListComponent
    },
    data() {
      return {
        sondages: []
      };
    },
    mounted() {
        const token = localStorage.getItem('token');

        if (token) {
            axios.get('http://127.0.0.1:8080/mes_sondages', {
            headers: {
                'Authorization': `${token}`
            }
            })
            .then(response => {
            this.sondages = response.data.sondages;
            })
            .catch(error => {
            console.error('Erreur lors de la récupération des sondages:', error);
            });
        }
    }
};
</script>
  