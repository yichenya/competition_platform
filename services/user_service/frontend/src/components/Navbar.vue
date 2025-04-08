<template>
    <nav class="navbar">
      <div class="nav-links">
        <a href="#">主页</a>
        <a href="#">竞赛报名与考试</a>
        <a href="#">雅思模拟</a>
        <a href="#">关于我们</a>
      </div>
      <div class="nav-actions">
        <a href="#">消息</a>
        <a href="#">我的</a>
      </div>
    </nav>
  </template>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f4f4f4;
    padding: 10px 20px;
  }
  .nav-links a,
  .nav-actions a {
    margin: 0 10px;
    text-decoration: none;
    color: #333;
  }
  .nav-links a:hover,
  .nav-actions a:hover {
    color: #007bff;
  }
  </style>