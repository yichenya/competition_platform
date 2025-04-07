<template>
    <div id="app">
      <nav>
        <router-link to="/register">注册</router-link>
        <router-link to="/login">登录</router-link>
        <router-link to="/user">用户详情</router-link>
      </nav>
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
  };
  </script>
  
  <style>
  #app {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0 auto;
    max-width: 800px;
  }
  nav {
    margin-bottom: 20px;
  }
  nav a {
    margin: 0 10px;
  }
  </style>