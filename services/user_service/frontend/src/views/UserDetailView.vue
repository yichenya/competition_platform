<template>
    <div>
      <h1>用户详情</h1>
      <p v-if="user">用户名：{{ user.username }}</p>
      <p v-if="user">邮箱：{{ user.email }}</p>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        user: null,
      };
    },
    async created() {
      try {
        const response = await api.getUserDetail();
        this.user = response.data;
      } catch (error) {
        alert('获取用户详情失败，请重试！');
        console.error(error);
      }
    },
  };
  </script>