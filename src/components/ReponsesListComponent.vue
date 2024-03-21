<template>
    <div class="object_item" v-for="reponse in reponses" :key="reponse._id">
        <router-link :to="{ name: 'reponse', params: { sondage_id: reponse.sondage_id, id: reponse._id } }">
        <h3>Réponse de</h3>
        <h3 v-if="isCreateur(reponse.utilisateur_id)">Moi</h3>
        <h3 v-else-if="utilExist(reponse.utilisateur_id)">{{ getNom(reponse.utilisateur_id) }}</h3>
        <h3 v-else>Inconnu</h3>
      </router-link>
    </div>
</template>

<script>
import axios from 'axios';
import VueJwtDecode from 'vue-jwt-decode'

export default {
  props: {
      reponses: {
          type: Array,
          required: true
      }
  },
    data() {
      return {
        utils: []
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
            alert("Une erreur s'est produite");
            this.$router.push('/');
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

<style scoped>
</style>