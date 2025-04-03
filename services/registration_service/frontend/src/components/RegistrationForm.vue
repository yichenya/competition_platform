<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="name">学生姓名：</label>
      <input v-model="form.name" id="name" required />
    </div>
    <div>
      <label for="student_id">学号：</label>
      <input v-model="form.student_id" id="student_id" required />
    </div>
    <div>
      <label for="grade">年级：</label>
      <input v-model="form.grade" id="grade" required />
    </div>
    <div>
      <label for="email">电子邮箱：</label>
      <input v-model="form.email" id="email" type="email" required />
    </div>
    <div>
      <label for="parent_name">家长姓名：</label>
      <input v-model="form.parent_name" id="parent_name" required />
    </div>
    <div>
      <label for="parent_phone">家长手机号：</label>
      <input v-model="form.parent_phone" id="parent_phone" type="tel" required />
    </div>
    <button type="submit">提交报名</button>
  </form>
</template>

<script>
import api from '../api';

export default {
  data() {
    return {
      form: {
        name: '',
        student_id: '',
        grade: '',
        email: '',
        parent_name: '',
        parent_phone: '',
      },
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await api.submitRegistration(this.form);
        alert('报名成功！');
        console.log(response.data);
      } catch (error) {
        alert('报名失败，请重试！');
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>