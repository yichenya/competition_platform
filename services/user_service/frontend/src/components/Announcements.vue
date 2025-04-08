<template>
    <div class="announcements">
      <h2>最新公告</h2>
      <ul>
        <li v-for="(announcement, index) in announcements" :key="index">
          <span>{{ announcement.date }}</span> - {{ announcement.text }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        announcements: [
          { date: "2024-03-15", text: "2024年英语竞赛报名通知" },
          { date: "2024-03-14", text: "雅思模拟考试时间安排" },
          { date: "2024-03-13", text: "在线课程更新通知" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .announcements {
    padding: 20px;
    background-color: #fff;
    margin: 20px auto;
    max-width: 800px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  .announcements ul {
    list-style: none;
    padding: 0;
  }
  .announcements li {
    margin: 10px 0;
  }
  .announcements span {
    font-weight: bold;
    color: #007bff;
  }
  </style>