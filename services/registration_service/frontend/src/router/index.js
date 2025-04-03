import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home, // 首页视图
  },
  {
    path: "/success",
    name: "Success",
    component: () => import("../views/Success.vue"), // 报名成功页面
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;