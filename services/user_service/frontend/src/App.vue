<template>
  <div id="app">
    <header class="header">
      <div class="banner">
        <h1>2024英语竞赛报名开始</h1>
        <p>立即参与，展现你的英语实力！</p>
      </div>
    </header>
    <nav class="navbar">
      <ul>
        <li><router-link to="/">主页</router-link></li>
        <li><router-link to="/competition">竞赛页面</router-link></li>
        <li><router-link to="/ielts">雅思模拟</router-link></li>
        <li><router-link to="/about">关于我们</router-link></li>
      </ul>
      <div class="navbar-right">
        <router-link to="/notifications">消息</router-link>
        <router-link to="/profile">我的</router-link>
      </div>
    </nav>
    <main>
      <section class="announcements">
        <h2>最新公告</h2>
        <ul>
          <li v-for="(announcement, index) in announcements" :key="index">
            <p>{{ announcement.title }}</p>
            <span>{{ announcement.date }}</span>
          </li>
        </ul>
      </section>
      <section class="carousel">
        <div v-for="(image, index) in images" :key="index" class="carousel-item">
          <img :src="image" alt="展示图片" />
        </div>
      </section>
    </main>
    <footer>
      <p>© 2025 英语竞赛报名系统</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      announcements: [
        { title: "2024年英语竞赛报名通知", date: "2024-03-15" },
        { title: "雅思模拟考试时间安排", date: "2024-03-14" },
        { title: "在线课程更新通知", date: "2024-03-13" },
      ],
      images: [
        "/assets/image1.jpg",
        "/assets/image2.jpg",
        "/assets/image3.jpg",
        "/assets/image4.jpg",
      ],
    };
  },
};
</script>

<style>
/* 样式代码 */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
.header .banner {
  background-color: #f4f4f4;
  padding: 20px;
  text-align: center;
}
.navbar {
  display: flex;
  justify-content: space-between;
  background-color: #007bff;
  padding: 10px 20px;
  color: white;
}
.navbar ul {
  list-style: none;
  display: flex;
  gap: 20px;
}
.navbar ul li {
  display: inline;
}
.navbar-right {
  display: flex;
  gap: 10px;
}
.announcements {
  padding: 20px;
}
.carousel {
  display: flex;
  overflow-x: auto;
  gap: 10px;
  padding: 20px;
}
.carousel-item img {
  width: 200px;
  height: 150px;
  object-fit: cover;
}
footer {
  text-align: center;
  padding: 10px;
  background-color: #f4f4f4;
}
</style>