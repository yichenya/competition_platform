import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8001/api', // 后端接口地址
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getCompetition() {
    return apiClient.get('/competition/');
  },
  submitRegistration(data) {
    return apiClient.post('/registration/', data);
  },
};