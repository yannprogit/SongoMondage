<template>
    <div v-for="reponse in reponses" :key="reponse._id">
        <router-link :to="{ name: 'reponse', params: { sondage_id: reponse.sondage_id, id: reponse._id } }">
        <h3>Réponse de</h3>
      <h3>{{ reponse.utilisateur_id }}</h3>
      </router-link>
    </div>
</template>

<script>
export default {
  props: {
      reponses: {
          type: Array,
          required: true
      }
  }
};
</script>

<style scoped>
</style>