<template>
    <div class="sondage">
      <h2>Mes Sondages</h2>
      <router-link to="/ajout-sondage">
        <button>Ajouter</button>
      </router-link>
      <SondageListComponent :sondages="sondages" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SondageListComponent from '@/components/SondageListComponent.vue';
  
  export default {
    name: 'SondageListView',
    components: {
      SondageListComponent
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
  