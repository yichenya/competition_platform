// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import RegisterView from '../views/RegisterView.vue';
import LoginView from '../views/LoginView.vue';
import UserDetailView from '../views/UserDetailView.vue';

const routes = [
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/user',
    name: 'UserDetail',
    component: UserDetailView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;