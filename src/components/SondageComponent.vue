<template>
    <div>
      <h3>{{ sondage.nom }}</h3>
      <div v-if="isCreateur()">
        <router-link :to="{ name: 'reponses', params: { id: sondage._id } }">Voir les réponses</router-link>
        <a>Modifier</a>
        <a @click="delSondage">Supprimer</a>
      </div>
      <form @submit.prevent="submitForm">
        <div v-for="question in sondage.questions" :key="question._id">
          <p>{{ question.intitule }}</p>
          <div v-if="question.type === 'qcm'">
            <div v-for="reponse in question.reponses" :key="reponse">
              <label>
                <input type="checkbox" :name="question._id" :value="reponse" />
                {{ reponse }}
              </label>
            </div>
          </div>
          <div v-else>
            <input type="text" :required="true" :id="question._id" />
          </div>
        </div>
        <button type="submit">Envoyer</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import VueJwtDecode from 'vue-jwt-decode'

  export default {
    props: {
      sondage: {
        type: Object,
        required: true
      }
    },
    methods: {
      delSondage() {
        const token = localStorage.getItem('token');
        if (token) {
          axios.delete(`http://127.0.0.1:8080/sondages/${this.sondage._id}`, {
            headers: {
              'Authorization': `${token}`,
            },
          })
          .then(() => {
            alert('Sondage supprimé !');
            this.$router.push('/mes-sondages');
          })
          .catch((error) => {
            console.log('Erreur lors de la suppression :', error);
          });
        } else {
          this.$router.push('/connexion');
        }
      },
      isCreateur() {
        const token = localStorage.getItem('token');
        if (token) {
          const decodedToken = VueJwtDecode.decode(token);
          return this.sondage.createur == decodedToken.id;
        } else {
          this.$router.push('/connexion');
        }
      },
      submitForm() {
        let qcmQuestions = this.sondage.questions.filter(question => question.type == 'qcm');

        for (let i = 0; i < qcmQuestions.length; i++) {
            let question = qcmQuestions[i];
            let checkedInputs = document.querySelectorAll(`input[type="checkbox"][name="${question._id}"]:checked`);
            if (checkedInputs.length == 0) {
                alert(`Vous devez cocher au moins une réponse pour la question "${question.intitule}"`);
                return;
            }
        }

        const token = localStorage.getItem('token');
        if (token) {
          let reponses = [];
          this.sondage.questions.forEach(question => {
            if (question.type == 'qcm') {
              let reponsesSelectionnees = Array.from(document.querySelectorAll(`input[type="checkbox"][name="${question._id}"]:checked`)).map(input => input.value);
              reponses.push({
                question_id: question._id,
                reponse: reponsesSelectionnees
              });
            } else {
              reponses.push({
                question_id: question._id,
                reponse: document.getElementById(question._id).value
              });
            }
          });
          const data = {
          reponses: reponses,
          };

          axios.post(`http://127.0.0.1:8080/sondages/${this.sondage._id}/reponse`, data, {
            headers: {
              'Authorization': `${token}`,
            },
          })
          .then(() => {
            alert('Réponses envoyées avec succès');
            this.$router.push('/');
          })
          .catch((error) => {
            console.log('Erreur lors de l\'envoi des réponses:', error);
          });
        } else {
          this.$router.push('/connexion');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  