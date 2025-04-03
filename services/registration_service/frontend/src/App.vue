<template>
    <div id="app">
      <header>
        <h1>英语竞赛报名系统</h1>
      </header>
      <main>
        <router-view /> <!-- 用于渲染路由对应的组件 -->
      </main>
      <footer>
        <p>© 2025 英语竞赛报名系统</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: "App",
  };
  </script>
  
  <style>
  #app {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0 auto;
    max-width: 800px;
  }
  header {
    background-color: #f4f4f4;
    padding: 20px;
    margin-bottom: 20px;
  }
  footer {
    margin-top: 20px;
    font-size: 0.9em;
    color: #666;
  }
  </style>