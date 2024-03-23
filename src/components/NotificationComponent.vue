<template>
    <div v-if="visible" class="notification-container">
      <div class="notification">
        <div class="message">{{ message }}</div>
        <button @click="closeNotification">OK</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: String,
      urlPage: String
    },
    data() {
      return {
        visible: true
      };
    },
    methods: {
      closeNotification() {
        this.visible = false;
        this.$emit('notificationClosed');
        if (this.urlPage!=null) {
            this.$router.push(this.urlPage);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .notification-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .notification {
    background-image: linear-gradient(to bottom, #edd504, orange);
    border: 2px solid #866508;
    color: #2c3e50;
    font-weight: bold;
    padding: 20px;
    border-radius: 15px;
  }
  
  .message {
    margin-bottom: 10px;
  }
  </style>
  