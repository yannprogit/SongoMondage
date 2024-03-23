<template>
    <div class="sondageForm">
      <router-link :to="{ name: 'mes-sondages'}"><button class="return-button">← Retour</button></router-link>
      <div class="background_bubble"><h2>Nouveau sondage</h2></div>
      <SondageFormComponent :mode="'add'"/>
    </div>
</template>
  
<script>
  import SondageFormComponent from '@/components/SondageFormComponent.vue';
  
  export default {
    name: 'AddSondageView',
    components: {
      SondageFormComponent
    }
};
</script>
  