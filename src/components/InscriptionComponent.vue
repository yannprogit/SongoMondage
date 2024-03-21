<template>
    <div class="background_base"></div>
    <div class="background_bubble_login">
      <h1>Page d'inscription</h1>
      <form @submit.prevent="inscription()">
        <table align="center" cellspacing="10">
          <tbody>
              <tr>
                  <td align="left"><label>Nom:</label></td>
                  <td align="left"><input type="text" v-model="nom" :required="true"></td>
              </tr>
              <tr>
                  <td align="left"><label>Mail:</label></td>
                  <td align="left"><input type="text" v-model="mail" :required="true"></td>
              </tr>
              <tr>
                  <td align="left"><label>Mot de passe:</label></td>
                  <td align="left"><input type="password" v-model="mdp" :required="true"></td>
              </tr>
          </tbody>
        </table>
        <button type="submit">S'incrire</button>
      </form>
      <p>Vous avez déjà un compte ? <router-link to="/connexion">connexion ici</router-link></p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        nom: '',
        mail: '',
        mdp: ''
      };
    },
    methods: {
      inscription() {
        const data = {
          nom: this.nom,
          mail: this.mail,
          mdp: this.mdp
        };
  
        axios.post(`http://127.0.0.1:8080/inscription`, data, {
              headers: {
                'Content-Type': 'application/json',
              },
            })
            .then(() => {
              alert('Votre compte a été crée avec succès !');
              this.$router.push('/connexion');
            })
            .catch(error => {
              if (error.response && error.response.status == 422) {
                alert(error.response.data.message);
              } else {
                alert('Une erreur est survenue lors de l\'inscription');
              }
            });
      }
    }
  };
  </script>
  
  <style>
  .background_base {
    margin-top:15%;
  }
  
  .background_bubble_login {
      background-color: #42b983;
      background-image: linear-gradient(to bottom, #42b983, #1fa694);
      border-radius: 15px;;
      padding: 10px;
      margin: 10px;
      max-width: 400px;
      margin-left: auto; 
      margin-right: auto;
      display: block;
      border: 2px solid #165c3d;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  }
  </style>
  