<template>
  <div>
    <form @submit.prevent="addSondage">
      <div>
        <div class="background_bubble">Nom du sondage : <input type="text" v-model="nom" :required="true"/></div>
        <div v-for="(question, questionIndex) in questions" :key="questionIndex" class="background_bubble">
          <div>
            Intitulé : <input type="text" v-model="question.intitule" :required="true"/>
          </div>
          <div>
            Type :
            <select v-model="question.type" @change="onTypeChange(question)">
              <option value="ouverte">Ouverte</option>
              <option value="qcm">QCM</option>
            </select>
          </div>
          <div v-if="question.type == 'qcm'">
            <div v-for="(reponse, reponseIndex) in question.reponses" :key="reponseIndex">
              Réponse {{ reponseIndex + 1 }} : <input type="text" v-model="question.reponses[reponseIndex]" :required="true"/>
              <button class="delete-button" v-if="reponseIndex+1>2" @click.prevent="delReponse(question, reponseIndex)">-</button>
            </div>
            <button @click.prevent="addReponse(question)">Ajouter une réponse</button>
          </div>
        </div>
        <button @click.prevent="addQuestion">Ajouter une question</button>
      </div>
      <br>
      <button type="submit">Créer</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
      mode: null
    },
  data() {
    return {
      nom: '',
      questions: [{ intitule: '', type: 'ouverte', reponses: ['',''] }]
    };
  },
  methods: {
    addSondage() {
      const token = localStorage.getItem('token');
      if (token) {
        let questionsWithoutBlankReponses = this.questions.map(question => {
          if (question.type=="ouverte") {
            delete question.reponses;
          }
          return question;
        });

        const data = {
          nom: this.nom,
          questions: questionsWithoutBlankReponses
        }
        
        axios.post(`http://127.0.0.1:8080/sondages`, data, {
            headers: {
              'Authorization': `${token}`,
            },
          })
          .then(() => {
            const router = this.$router;
            alert('Votre sondage a bien été ajouté !');
            router.push('/mes-sondages');
          })
          .catch((error) => {
            console.log('Erreur lors de l\'ajout du sondage :', error);
          });
      }
    },
    addQuestion() {
      this.questions.push({ intitule: '', type: 'ouverte', reponses: ['',''] });
    },
    delQuestion(questionIndex) {
      this.questions.splice(questionIndex, 1);
    },
    onTypeChange(question) {
      if (question.type != 'qcm') {
        question.reponses = [''];
      }
    },
    addReponse(question) {
      question.reponses.push('');
    },
    delReponse(question, reponseIndex) {
      question.reponses.splice(reponseIndex, 1);
    }
  }
};
</script>

<style scoped>
.delete-button {
  background-color: #8f2020;
    color: white;
    border: 2px solid transparent;
    border-radius: 5px;
    padding: 5px 10px 5px 10px; 
    cursor: pointer;
    font-weight: bold; 
    letter-spacing: 1px; 
    transition: background-color 0.3s ease; 
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.delete-button:hover {
  background-color: transparent;
    border-color: #8f2020; 
    color: #8f2020; 
}
</style>
