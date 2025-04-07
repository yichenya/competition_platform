<template>
    <div>
      <h1>登录</h1>
      <form @submit.prevent="login">
        <label for="username">用户名：</label>
        <input v-model="form.username" id="username" required />
        <br />
        <label for="password">密码：</label>
        <input v-model="form.password" id="password" type="password" required />
        <br />
        <button type="submit">登录</button>
      </form>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
      };
    },
    methods: {
      async login() {
        try {
          const response = await api.loginUser(this.form);
          alert('登录成功！');
          console.log(response.data);
        } catch (error) {
          alert('登录失败，请重试！');
          console.error(error);
        }
      },
    },
  };
  </script>