<template>
    <div>
      <Header />
      <Navbar />
      <Announcements />
      <ImageCarousel />
    </div>
  </template>
  
  <script>
  import Header from "../components/Header.vue";
  import Navbar from "../components/Navbar.vue";
  import Announcements from "../components/Announcements.vue";
  import ImageCarousel from "../components/ImageCarousel.vue";
  
  export default {
    components: {
      Header,
      Navbar,
      Announcements,
      ImageCarousel,
    },
  };
  </script>