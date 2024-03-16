<template>
    <div class="sondage">
      <SondageComponent :sondages="sondages" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SondageComponent from '@/components/SondageComponent.vue';
  
  export default {
    name: 'SondageView',
    components: {
      SondageComponent
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
            .catch(error => {
            console.error('Erreur lors de la récupération des sondages:', error);
            });
        }
    }
};
</script>
  