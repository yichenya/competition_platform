<template>
    <div>
      <CompetitionInfo />
      <RegistrationForm />
    </div>
  </template>
  
  <script>
  import CompetitionInfo from "../components/CompetitionInfo.vue";
  import RegistrationForm from "../components/RegistrationForm.vue";
  
  export default {
    components: {
      CompetitionInfo,
      RegistrationForm,
    },
  };
  </script>