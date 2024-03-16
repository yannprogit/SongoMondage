<!-- SondageDetails.vue -->
<template>
    <div>
      <div v-if="sondage">
        <h3>{{ sondage.nom }}</h3>

        <form @submit.prevent="submitForm">
          <div v-for="question in sondage.questions" :key="question._id">

          <p>{{ question.intitule }}</p>
          <div v-if="question.type=='qcm'">
            <div v-for="reponse in question.reponses" :key="reponse">
            <label >
              <input
              type="checkbox"
              :name="question._id"
              :value="reponse"
              />
              {{ reponse }}
            </label>
            </div>
          </div>
          <div v-else>
            <input type="text" :required="true" :id="question._id"/>
          </div>
        </div>
        <button type="submit">Envoyer</button>
        </form>
      </div>
      <div v-else>
        <p>Le sondage n'a pas été trouvé.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      id: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        sondage: null,
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
    },
    methods: {
      submitForm() {
        let qcmQuestions = this.sondage.questions.filter(question => question.type === 'qcm');

        for (let i = 0; i < qcmQuestions.length; i++) {
            let question = qcmQuestions[i];
            let checkedInputs = document.querySelectorAll(`input[type="checkbox"][name="${question._id}"]:checked`);
            if (checkedInputs.length === 0) {
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
          axios.post(`http://127.0.0.1:8080/sondages/${this.id}/reponse`, data, {
            headers: {
              'Authorization': `${token}`,
            },
          })
          .then(() => {
            alert('Réponses envoyées avec succès');
          })
          .catch((error) => {
            alert('Erreur lors de l\'envoi des réponses:', error);
          });
        }
      }
    }
  };
</script>
  
  <style scoped>
  </style>
  