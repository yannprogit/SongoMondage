<template>
    <div>
      <router-link :to="{ name: 'reponses', params: { id: sondage._id }}"><button class="return-button">← Retour</button></router-link>
      <div class="background_bubble"><h3>{{ sondage.nom }}</h3></div>
        <div v-for="(question, questionIndex) in sondage.questions" :key="questionIndex" class="background_bubble">
          <p>{{ question.intitule }}</p>
          <div v-if="question.type == 'qcm'">
            <table align="center">
              <tbody>
                  <tr v-for="qReponse in question.reponses" :key="qReponse">
                      <td><input type="checkbox" :value="qReponse" :checked="reponse.reponses[questionIndex].reponse.includes(qReponse)" disabled/></td>
                      <td align="left"><label>{{ qReponse }}</label></td>
                  </tr>
              </tbody>
            </table>
          </div>
          <div v-else>
            <input type="text" :value="reponse.reponses[questionIndex].reponse" disabled/> 
          </div>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      sondage: {
        type: Object,
        required: true
      },
      reponse: {
        type: Object,
        required: false
      },
    }
  };
  </script>
  
<style scoped>
input[type="text"]:disabled {
  color: initial; 
} 
</style>
