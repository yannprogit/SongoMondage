<template>
      <div class="object_item" v-for="sondage in sondages" :key="sondage._id">
        <router-link :to="{ name: 'sondage', params: { id: sondage._id } }">
        <h3>{{ sondage.nom }}</h3>
        <p>Créateur: {{ sondage.createur }}</p>
        <p>Nombre de questions: {{ sondage.questions.length }}</p>
        </router-link>
      </div>
</template>
  
  <script>
  export default {
    props: {
        sondages: {
            type: Array,
            required: true
        }
    }
  };
  </script>
  