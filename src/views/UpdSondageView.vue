<template>
    <div class="sondageForm">
      <div v-if="sondage">
        <div class="background_bubble"><h2>Modification d'un sondage</h2></div>
        <SondageFormComponent :mode="'upd'" :sondage="sondage" />
      </div>
      <div v-else class="background_bubble">
        <p>Le sondage n'a pas été trouvé</p>
      </div>
    </div>
</template>
  
<script>
  import axios from 'axios';
  import SondageFormComponent from '@/components/SondageFormComponent.vue';
  
  export default {
    name: 'UpdSondageView',
    components: {
      SondageFormComponent
    },
    props: {
      id: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        sondage: null
      };
    },
    mounted() {
      const token = localStorage.getItem('token');
      if (token) {
        axios.get(`http://127.0.0.1:8080/sondages/${this.id}`, {
          headers: {
            'Authorization': `${token}`
          }
        })
        .then(response => {
          this.sondage = response.data.sondage;
        })
        .catch(error => {
          console.error('Erreur lors de la récupération du sondage:', error);
        });
      }
    }
};
</script>
  