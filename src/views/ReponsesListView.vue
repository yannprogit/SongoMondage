<template>
    <div class="reponse">
      <div v-if="reponses.length!=0">
        <router-link :to="{ name: 'sondage', params: { id: id }}"><button class="return-button">← Retour</button></router-link>
        <div class="background_bubble">
          <h2>Liste des réponses</h2>
          <p>Nombre de réponses : {{ reponses.length }}</p>
        </div><br>
        <ReponsesListComponent :reponses="reponses" />
      </div>
      <div v-else>
        <router-link :to="{ name: 'sondage', params: { id: id }}"><button class="return-button">← Retour</button></router-link>
        <div class="background_bubble">
          <p>Aucune réponses</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import ReponsesListComponent from '@/components/ReponsesListComponent.vue';
  
  export default {
    name: 'ReponseListView',
    components: {
      ReponsesListComponent
    },
    props: {
        id: {
        type: String,
        required: true
        }
    },
    data() {
      return {
        reponses: []
      };
    },
    mounted() {
        const token = localStorage.getItem('token');

        if (token) {
            axios.get(`http://127.0.0.1:8080/sondages/${this.id}/reponses`, {
            headers: {
                'Authorization': `${token}`
            }
            })
            .then(response => {
            this.reponses = response.data.reponses;
            })
            .catch(error => {
            if (error.response && error.response.status == 403) {
              this.$router.push(`/sondages/${this.id}`);
            }
            this.reponses = [];
            });
        }
    }
};
</script>
  