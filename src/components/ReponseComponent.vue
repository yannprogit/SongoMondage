<template>
    <div>
      <h3>{{ sondage.nom }}</h3>
        <div v-for="(question, questionIndex) in sondage.questions" :key="questionIndex">
          <p>{{ question.intitule }}</p>
          <div v-if="question.type == 'qcm'">
            <div v-for="qReponse in question.reponses" :key="qReponse">
              <label>
                <input type="checkbox" :value="qReponse" :checked="reponse.reponses[questionIndex].reponse.includes(qReponse)" disabled/> 
                {{ qReponse }}
              </label>
            </div>
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
  </style>
