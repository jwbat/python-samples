<template>
  <div class="container">
    <div
      v-for="num in 100"
      :key="num"
      class="item"
    ></div> 
  </div> 
</template>

<script>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

import { hsl, rand } from '../util/funcs.js';

export default {
  setup() {
    onMounted(() => {
      gsap.from('.item', {
        duration: 1,
        x: 'random(-200, 200)',
        y: 'random(-200, 200)',
        stagger: 0.05,
        ease: 'power2'
      })
      gsap.to('.item', {
        duration: 1,
        opacity: 1,
        y: 100,
        stagger: 0.05,
        backgroundColor: () => ['black', hsl()][rand(2)()],
      })
      const tl = gsap.timeline({ repeat: 1, yoyo: true });
      tl.to('.item', {
//        delay: 1,
        duration: 1,
        backgroundColor: () => [
          'turquoise', 'crimson', 'cornflower', 'black', 'black'
        ][rand(5)()],
        borderRadius: '50%',
        y: () => [-100, 300][rand(2)()],
        stagger: 0.1,
      })
        .to('.item', {
        duration: 1,
        x: () => [-200, 200][rand(2)()],
        scale: () => [0.5, 0.2, 0.8, 2][rand(4)()],
        stagger: 0.05,
        ease: 'power2',
      })
    });
  }
}
</script>

<style scoped>
.container {
  padding: 10rem 15rem; 
  height: 100vh;
  width: 100vw;
  background: black;
}

.item {
  display: inline-block;
  opacity: 0;
  margin: 0.5rem;
  width: 2rem;
  height: 2rem;
  background: yellow;
}
</style>

