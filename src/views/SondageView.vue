<template>
  <div>
    <div v-if="sondage">
      <SondageComponent :sondage="sondage" />
    </div>
    <div v-else class="background_bubble">
      <router-link :to="{ name: 'sondages'}"><button class="return-button">← Retour</button></router-link>
      <p>Le sondage n'a pas été trouvé</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SondageComponent from '@/components/SondageComponent.vue';

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  components: {
    SondageComponent
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
      .catch(() => {
        this.sondage = null;
      });
    }
  }
};
</script>
  
  <style scoped>
  </style>
  