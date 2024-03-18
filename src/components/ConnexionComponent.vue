<template>
  <div>
    <h1>Page de Connexion</h1>
    <form @submit.prevent="login">
      <label for="mail">Mail:</label>
      <input type="text" v-model="mail" :required="true">
      <br>
      <label for="mdp">Mot de passe:</label>
      <input type="password" v-model="mdp" :required="true">
      <br>
      <button type="submit">Se connecter</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      mail: '',
      mdp: ''
    };
  },
  methods: {
    login() {
      const data = {
        mail: this.mail,
        mdp: this.mdp
      };

      axios.post(`http://127.0.0.1:8080/connexion`, data, {
            headers: {
              'Content-Type': 'application/json',
            },
          })
          .then(response => {
            const token = response.data.token;
            localStorage.setItem('token', token);
            this.$router.push('/');
          })
          .catch((error) => {
            console.log('Erreur lors de la connexion :', error);
          });
    }
  }
};
</script>

<style scoped>
</style>
