<template>
    <div class="carousel">
      <div class="carousel-images">
        <img :src="images[currentImage]" alt="轮播图片" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          "@/assets/images/image1.jpg",
          "@/assets/images/image2.jpg",
          "@/assets/images/image3.jpg",
          "@/assets/images/image4.jpg",
        ],
        currentImage: 0,
      };
    },
    mounted() {
      setInterval(() => {
        this.currentImage = (this.currentImage + 1) % this.images.length;
      }, 3000); // 每3秒切换图片
    },
  };
  </script>
  
  <style scoped>
  .carousel {
    margin: 20px auto;
    max-width: 800px;
    overflow: hidden;
    border-radius: 5px;
  }
  .carousel-images img {
    width: 100%;
    display: block;
  }
  </style>