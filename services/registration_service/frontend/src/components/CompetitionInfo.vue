<template>
  <div class="competition-info">
    <h2>{{ competition.name }}</h2>
    <p>比赛时间：{{ competition.start_date }} - {{ competition.end_date }}</p>
    <p>报名截止：{{ competition.registration_deadline }}</p>
    <p>{{ competition.description }}</p>
  </div>
</template>

<script>
import api from '../api';

export default {
  data() {
    return {
      competition: {},
    };
  },
  async created() {
    const response = await api.getCompetition();
    this.competition = response.data;
  },
};
</script>

<style scoped>
.competition-info {
  margin-bottom: 20px;
}
</style>