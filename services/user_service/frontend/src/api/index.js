// src/api/index.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // user_service 的后端 API 地址
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  registerUser(data) {
    return apiClient.post('/register/', data);
  },
  loginUser(data) {
    return apiClient.post('/login/', data);
  },
  getUserDetail() {
    return apiClient.get('/user/');
  },
};