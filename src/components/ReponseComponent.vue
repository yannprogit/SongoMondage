<template>
    <div>
      <div class="background_bubble"><h3>{{ sondage.nom }}</h3></div>
        <div v-for="(question, questionIndex) in sondage.questions" :key="questionIndex" class="background_bubble">
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
input[type="text"]:disabled {
  color: initial; 
} 
</style>
