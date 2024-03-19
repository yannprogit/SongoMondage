<template>
    <div class="sondageForm">
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
  