<template>
  <div class="container">
    <div class="box">
      <div
        v-for="num in 4"
        :key="num"
        class="item"
      ></div> 
    </div> 
  </div> 
</template>

<script>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

export default {
  setup() {

    onMounted(play);
    
    function play() {
      const tl = gsap.timeline({ repeat: 1, yoyo: true });
      tl.fromTo('.box', {
          scale: 0.5
        }, 
        {
          duration: 2,
          scale: 2.5,
          ease: 'power2.inOut',
        })
        .to('.item', {
          duration: 1,
          stagger: 0.5,
          backgroundColor: idx => ['red', 'yellow', 'blue', 'green'][idx],
        })
        .to('.item', {
          duration: 1,
          x: idx => idx % 2 ? '5rem' : '-5rem',
          y: idx => idx < 2 ? '-5rem' : '5rem',
        })
        .to('.box', {
          duration: 1,
          scale: 2,
        })
        .to('.item', {
          delay: 1,
          duration: 2,
          rotation: 270,
          stagger: 0.5,
          ease: 'power2.inOut'
        },
          '<'
        )
        .to('.item', {
          duration: 2,
          x: idx => idx % 2 ? '-8rem' : '8rem',
          ease: 'power2.inOut'
        })
        .to('.item', {
          duration: 3,
          y: idx => idx < 2 ? '8rem' : '-8rem',
          ease: 'elastic.inOut'
        })
        .to('.item', {
          duration: 2,
          x: idx => idx % 2 ? '7rem' : '-7rem',
          y: idx => idx < 2 ? '-7rem' : '7rem',
          ease: 'power3.inOut'
        })
        .to('.box', {
          duration: 3,
          rotation: 90,
        })
    }
  }
}
</script>

<style scoped>
.container {
  padding: 10rem 15rem; 
  height: 100vh;
  width: 100vw;
  background: black;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
  border: 1px solid purple;
  width: 10vmin;
  height: 10vmin;
  display: grid;
  grid-template-columns: 50% 50%;
}

.item {
  display: inline-block;
  border: 1px solid maroon;
  background: grey;
}
</style>

