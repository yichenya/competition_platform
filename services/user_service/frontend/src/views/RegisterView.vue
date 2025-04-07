<template>
    <div>
      <h1>注册</h1>
      <form @submit.prevent="register">
        <label for="username">用户名：</label>
        <input v-model="form.username" id="username" required />
        <br />
        <label for="email">邮箱：</label>
        <input v-model="form.email" id="email" type="email" required />
        <br />
        <label for="password">密码：</label>
        <input v-model="form.password" id="password" type="password" required />
        <br />
        <button type="submit">注册</button>
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
          email: '',
          password: '',
        },
      };
    },
    methods: {
      async register() {
        try {
          const response = await api.registerUser(this.form);
          alert('注册成功！');
          console.log(response.data);
        } catch (error) {
          alert('注册失败，请重试！');
          console.error(error);
        }
      },
    },
  };
  </script>