<template>
    <div class="sondageForm">
      <h2>Nouveau sondage</h2>
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
  