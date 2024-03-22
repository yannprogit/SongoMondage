<template>
    <div class="sondage">
      <div v-if="sondages.length!=0">
        <div class="background_bubble"><h2>Liste des Sondages</h2></div><br>
        <SondagesListComponent :sondages="sondages" />
      </div>
      <div v-else>
        <p class="background_bubble">Aucun sondages</p>
      </div>
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
            axios.get('http://127.0.0.1:8080/sondages', {
            headers: {
                'Authorization': `${token}`
            }
            })
            .then(response => {
            this.sondages = response.data.sondages;
            })
            .catch(() => {
            this.sondages = [];
            });
        }
    }
};
</script>
  