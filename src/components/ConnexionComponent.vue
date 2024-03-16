<template>
  <div>
    <h1>Page de Connexion</h1>
    <form @submit.prevent="handleLogin">
      <label for="mail">Mail:</label>
      <input type="text" v-model="mail" required>
      <br>
      <label for="mdp">Mot de passe:</label>
      <input type="password" v-model="mdp" required>
      <br>
      <button type="submit">Se connecter</button>
    </form>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      mail: '',
      mdp: '',
      router: useRouter()
    };
  },
  methods: {
    async handleLogin() {
      const router = this.$router;
      const loginData = {
        mail: this.mail,
        mdp: this.mdp
      };

      try {
        const response = await fetch('http://127.0.0.1:8080/connexion', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(loginData)
        });

        if (response.ok) {
          let responseData = await response.json();
            // Gérer la réponse réussie ici
            console.log('Connexion réussie!');
            localStorage.setItem('token', responseData.token);
            this.$root.login();
            router.push('/about');
          } else {
            console.error('Réponse invalide ou token manquant.');
          }
      } catch (error) {
        console.error('Erreur lors de la connexion:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Styles spécifiques au composant */
</style>
