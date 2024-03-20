<template>
    <div class="accueil">
        <AccueilComponent/>
    </div>
</template>

<script>
  import AccueilComponent from '@/components/AccueilComponent.vue';
  
  export default {
        name: 'AccueilView',
        components: {
            AccueilComponent
        }
    }
</script>