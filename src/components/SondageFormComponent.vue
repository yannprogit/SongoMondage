<template>
  <div v-if="mode=='add'">
    <form @submit.prevent="addSondage">
      <div>
        <div class="background_bubble">Nom du sondage : <input type="text" v-model="nom" :required="true"/></div>
        <div v-for="(question, questionIndex) in questions" :key="questionIndex" class="background_bubble">
          <div>
            <h3 class="question-title">Question {{ questionIndex + 1 }}</h3>
            <button class="delete-button" v-if="questionIndex+1>1" @click.prevent="delQuestion(questionIndex)">-</button>
          </div>
          <table align="center" cellspacing="10">
            <tbody>
              <tr>
                <td align="left">Intitulé : </td>
                <td align="left"><input type="text" v-model="question.intitule" :required="true"/></td>
              </tr>
              <tr>
                <td align="left">Type :</td>
                <td align="left">
                  <select v-model="question.type" @change="onTypeChange(question)">
                    <option value="ouverte">Ouverte</option>
                    <option value="qcm">QCM</option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>
          <div v-if="question.type == 'qcm'">
            <table align="center">
              <tbody>
                <tr v-for="(reponse, reponseIndex) in question.reponses" :key="reponseIndex">
                  <td align="left">Réponse {{ reponseIndex + 1 }} :</td>
                  <td align="left">
                    <input type="text" v-model="question.reponses[reponseIndex]" :required="true"/>
                    <button class="delete-button" v-if="reponseIndex+1>2" @click.prevent="delReponse(question, reponseIndex)">-</button>
                  </td>
                </tr>
              </tbody>
            </table>
            <button @click.prevent="addReponse(question)">Ajouter une réponse</button>
          </div>
        </div>
        <button @click.prevent="addQuestion">Ajouter une question</button>
      </div>
      <br>
      <button type="submit">Créer</button>
    </form>
  </div>


  <div v-else>
    <form @submit.prevent="updSondage">
      <div>
        <div class="background_bubble">Nom du sondage : <input type="text" v-model="nom" :required="true"/></div>
        <div v-for="(question, questionIndex) in questions" :key="questionIndex" class="background_bubble">
          <div>
            <h3 class="question-title">Question {{ questionIndex + 1 }}</h3>
            <button class="delete-button" v-if="questionIndex+1>1" @click.prevent="delQuestion(questionIndex)">-</button>
          </div>
          <table align="center" cellspacing="10">
            <tbody>
              <tr>
                <td align="left">Intitulé : </td>
                <td align="left"><input type="text" v-model="question.intitule" :required="true"/></td>
              </tr>
              <tr>
                <td align="left">Type :</td>
                <td align="left">
                  <select v-model="question.type" @change="onTypeChange(question)">
                    <option value="ouverte">Ouverte</option>
                    <option value="qcm">QCM</option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>
          <div v-if="question.type == 'qcm'">
            <table align="center">
              <tbody>
                <tr v-for="(reponse, reponseIndex) in question.reponses" :key="reponseIndex">
                  <td align="left">Réponse {{ reponseIndex + 1 }} :</td>
                  <td align="left">
                    <input type="text" v-model="question.reponses[reponseIndex]" :required="true"/>
                    <button class="delete-button" v-if="reponseIndex+1>2" @click.prevent="delReponse(question, reponseIndex)">-</button>
                  </td>
                </tr>
              </tbody>
            </table>
            <button @click.prevent="addReponse(question)">Ajouter une réponse</button>
          </div>
        </div>
        <button @click.prevent="addQuestion">Ajouter une question</button>
      </div>
      <br>
      <button type="submit">Modifier</button>
    </form>
  </div>
  <notification :message="notificationMessage" :urlPage="urlPageNotification" v-if="showNotification" @notificationClosed="showNotification = false"/>
</template>

<script>
import axios from 'axios';
import VueJwtDecode from 'vue-jwt-decode';
import Notification from './NotificationComponent.vue';

export default {
  props: {
      mode: null,
      sondage: {
        type: Object,
        required: function() {
          return this.mode == 'upd';
        }
      }
    },
  components: {
    Notification
  },
  data() {
    return {
      nom: '',
      questions: [{ intitule: '', type: 'ouverte', reponses: ['',''] }],
      showNotification: false,
      notificationMessage: '',
      urlPageNotification: null
    };
  },
  created() {
    if (this.mode=="upd") {
      const token = localStorage.getItem('token');
      const decodedToken = VueJwtDecode.decode(token);
      if (this.sondage.createur == decodedToken.id) {
        this.nom = this.sondage.nom;
        this.questions.splice(0, 1);
        this.sondage.questions.forEach(question => {
          if (question.type == "ouverte") {
            question.reponses = ['', ''];
          }
        this.questions.push(question);
        });
      } else {
        this.$router.push(`/sondages/${this.sondage._id}`);
      }
    }
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
            this.showNotification = true;
            this.notificationMessage = 'Sondage a bien été ajouté !';
            this.urlPageNotification = '/mes-sondages';
          })
          .catch(error => {
            if (error.response && error.response.status == 422) {
              this.showNotification = true;
              this.notificationMessage = error.response.data.message;
            } else {
              this.showNotification = true;
              this.notificationMessage = "Une erreur s'est produite lors de l'ajout du sondage";
            }
          });
      }
    },
    updSondage() {
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

        axios.put(`http://127.0.0.1:8080/sondages/${this.sondage._id}`, data, {
            headers: {
              'Authorization': `${token}`,
            },
          })
          .then(() => {
            this.showNotification = true;
            this.notificationMessage = 'Votre sondage a bien été modifié !';
            this.urlPageNotification = `/sondages/${this.sondage._id}`;
          })
          .catch((error) => {
            if (error.response && error.response.status == 422) {
              this.showNotification = true;
              this.notificationMessage = error.response.data.message;
            } else {
              this.showNotification = true;
              this.notificationMessage = "Une erreur s'est produite lors de la mise à jour du sondage";
            }
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
.question-title {
  display: inline;
  margin-right: 10px; 
}

.delete-button {
  background-color: #b62a2a;
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
    border-color: #b62a2a; 
    color: #b62a2a; 
}
</style>
