<template>
    <div>
      <div v-if="sondage && reponse">
        <ReponseComponent :sondage="sondage" :reponse="reponse"/>
      </div>
      <div v-else class="background_bubble">
        <p>La réponse n'a pas été trouvé.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import ReponseComponent from '@/components/ReponseComponent.vue';
  
  export default {
    props: {
      id: {
        type: String,
        required: true
      },
      sondage_id: {
        type: String,
        required: true
      }
    },
    components: {
      ReponseComponent
    },
    data() {
      return {
        sondage: null,
        reponse: null
      };
    },
    mounted() {
      const token = localStorage.getItem('token');
      if (token) {
        axios.get(`http://127.0.0.1:8080/sondages/${this.sondage_id}`, {
        headers: {
          'Authorization': `${token}`
            }
        })
        .then(response => {
            this.sondage = response.data.sondage;
        })
        .catch(() => {
            this.sondage = null;
        });
        
        axios.get(`http://127.0.0.1:8080/sondages/${this.sondage_id}/reponses/${this.id}`, {
          headers: {
            'Authorization': `${token}`
          }
        })
        .then(response => {
          this.reponse = response.data.reponse;
        })
        .catch(() => {
          this.reponse = null;
        });
      }
    }
  };
  </script>