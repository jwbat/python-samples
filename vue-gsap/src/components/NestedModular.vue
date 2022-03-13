<template>
  <div class="container">
    <div
      v-for="num in 1"
      :key="num"
      class="item"
      ></div> 
  </div> 
</template>

<script>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

import { hsl } from '../util/funcs.js';

export default {
  setup() {

    onMounted(play);
    
    function play() {

      function one() {
        const tl = gsap.timeline({ 
          defaults: { duration: 2, ease: 'power2.inOut' }
        });
        tl
          .to('.item', {
            x: '+=70vw'
          })
          .to('.item', {
            y: '+=70vh'
          })
          .to('.item', {
            x: '-=70vw',
          })
          .to('.item', {
            y: '-=70vh',
          })
        return tl;
      }

      function two() {
        const tl = gsap.timeline();
        tl
          .to('.item', {
            duration: 1,
            backgroundColor: hsl(),
            rotateY: 360,
          })
        return tl;
      }

      const master = gsap.timeline();
      master.add(one());
      master.add(two());
      master.add(one());
      master.add(two());
    }
  }
}
</script>

<style scoped>
.container {
  height: 100vh;
  width: 100vw;
  background: black;
  position: relative;
}

.item {
  position: absolute;
  top: 10vh;
  left: 10vw;
  border: 0.5px solid bisque;
  background: rgba(0, 50, 200, 0.8);
  width: 10vmin;
  height: 10vmin;
}
</style>

