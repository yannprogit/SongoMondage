<template>
  <nav>
    <router-link to="/">Sondages</router-link>
    <router-link to="/mes-sondages">Mes sondages</router-link>
    <router-link to="/about">About</router-link>
    <button @click="logout">Déconnexion</button>
  </nav>
  <router-view/>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: false,
    };
  },
  methods: {
    login() {
      this.isLoggedIn = true;
    },
    logout() {
      this.isLoggedIn = false;
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
