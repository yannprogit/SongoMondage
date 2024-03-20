<template>
    <div>
      <div class="background_bubble"><h3>{{ sondage.nom }}</h3></div>
      <div v-if="isCreateur()" class="sondage_menu">
        <router-link :to="{ name: 'reponses', params: { id: sondage._id } }">Réponses</router-link>
        <router-link :to="{ name: 'reponses', params: { id: sondage._id } }">Modifier</router-link>
        <a @click="delSondage">Supprimer</a>
      </div>
      <form @submit.prevent="submitForm">
        <div v-for="question in sondage.questions" :key="question._id" class="background_bubble">
          <p>{{ question.intitule }}</p>
          <div v-if="question.type == 'qcm'">
            <table align="center">
              <tbody>
                  <tr v-for="reponse in question.reponses" :key="reponse">
                      <td><input type="checkbox" :name="question._id" :value="reponse" /></td>
                      <td align="left"><label>{{ reponse }}</label></td>
                  </tr>
              </tbody>
            </table>
          </div>
          <div v-else>
            <input type="text" :required="true" :id="question._id" autocomplete="off"/>
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
            alert('Une erreur est survenue lors de la suppression');
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
.sondage_menu {
  background-image: linear-gradient(to bottom, #13b4a4, #207D8F);
  padding: 10px 10px 10px 10px;
  text-align: center;
  display: inline-block;
  border-radius: 15px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.sondage_menu a {
  text-decoration: none;
  padding: 0 5px;
  font-weight: bold;
  color: #2c3e50;
  transition: color 0.3s ease-in-out, text-decoration 3s ease-in-out;
}

.sondage_menu a:hover {
  color: #edd504;
  text-decoration: underline;
}
</style>
  