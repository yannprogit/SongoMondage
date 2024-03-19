<template>
  <div class="menu_base"></div>
  <nav>
    <img src="./assets/logo.png" alt="Logo de votre site">
    <router-link to="/about">Accueil</router-link>
    <router-link to="/">Sondages</router-link>
    <router-link to="/mes-sondages">Mes sondages</router-link>
    <a @click="logout">Déconnexion</a>
  </nav>
  <router-view/>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/connexion');
    },
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu_base {
  top: 2px;
  padding: 40px;
}

.background_bubble {
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

button {
    background-color: #207D8F;
    color: white;
    border: 2px solid transparent;
    border-radius: 25px;
    padding: 5px 20px; 
    cursor: pointer;
    font-weight: bold; 
    letter-spacing: 1px; 
    transition: background-color 0.3s ease; 
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

button:hover {
    background-color: transparent;
    border-color: #207D8F; 
    color: #207D8F; 
}

input[type="text"], input[type="password"] {
    background-color: #43c088;
    border: none;
    border-radius: 5px; 
    padding: 5px;
    border: 2px solid transparent;
    appearance: none;
}

input[type="checkbox"] {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    border: 2px solid #E6DD2B;
    border-radius: 3px;
    position: relative;
    top: 1px;
}

input[type="checkbox"]:checked {
    background-color: transparent;
}

input[type="checkbox"]::before {
    content: "\2713"; 
    font-size: 12px; 
    color: #E6DD2B; 
    position: absolute;
    font-weight: bold;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: none; 
}

input[type="checkbox"]:checked::before {
    display: block;
}

input[type="text"]:focus ,input[type="password"]:focus {
  border: 2px solid rgb(236, 224, 3);  
  outline: none; 
}

.object_item {
  background-color: #42b983;
  background-image: linear-gradient(to bottom, #42b983, #1fa694);
  border-radius: 15px;
  padding: 10px;
  margin: 10px;
  max-width: 400px;
  margin-left: auto; 
  margin-right: auto;
  display: block;
  border: 2px solid #165c3d;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s ease; 
}

.object_item:hover {
  border-color: #edd504;
}

.object_item a {
  color: #2c3e50;
  text-decoration: none;
}

nav {
  position: fixed;
  background-image: linear-gradient(to bottom, #edd504, orange);
  top: 2px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 10px 10px 10px;
  text-align: center;
  display: inline-block;
  border-radius: 15px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

nav a {
  text-decoration: none;
  padding: 0 5px;
  font-weight: bold;
  color: #2c3e50;
  transition: color 0.3s ease-in-out, text-decoration 3s ease-in-out;
}

nav a:hover {
  color: #207D8F;
  text-decoration: underline;
}

nav img {
  vertical-align: middle;
  margin: 0 5px;
  width: 50px;
}

nav a.router-link-exact-active {
  color: #207D8F;
  text-decoration: underline;
}

body {
  background-color: #05A69C;
  background-image: url('./assets/background.png');
}
</style>
