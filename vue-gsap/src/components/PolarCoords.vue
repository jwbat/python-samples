<template>
  <div class="container">
    <div class="box">
      <div
        v-for="num in nrs"
        :key="num"
        class="item"
      ></div>
    </div> 
  </div> 
</template>

<script>
import { ref, onMounted, onUpdated, } from 'vue';
import { gsap } from 'gsap';
import { hsl, rand } from '../util/funcs.js';

export default {
  setup() {
    const pi = Math.PI;
    const cos = Math.cos;
    const sin = Math.sin;

    const nrs = ref(3);

    onMounted(play);
    onUpdated(play);
    
    function play() {
      const diameter = (30 / nrs.value + 1) + 'rem';
      const theta = 2 * pi / nrs.value;
      const radius = nrs.value + 3;
      const colors = Array.from({ length: 3 }).map(() => hsl());

      const tl = gsap.timeline();
      tl
        .fromTo(['.box', '.item'],
        {
          opacity: 0,
        },
        {
          duration: 1,
          opacity: 1,
          width: diameter,
          height: diameter,
          ease: 'power1.inOut',
        })
        .to('.item', {
          duration: 3,
          backgroundColor: () => colors[rand(3)()],
          x: idx => radius * cos(idx * theta) + 'rem',
          y: idx => radius * sin(idx * theta) + 'rem',
          ease: 'back.inOut',
        })
        .to('.item', {
          duration: 1, x: 0, y: 0, ease: 'power3.inOut',
          opacity: 0,
          onComplete: function() {
            nrs.value = Math.max(3, (nrs.value + 2) % 25);
          }
        })
    }
    return { nrs };
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
/*   border: 1px solid purple;*/
  opacity: 0;
  position: relative;
  border-radius: 50%;
}

.item {
  display: inline-block;
  background: beige;
  position: absolute;
  top: 50%;
  left: 50%;
  border-radius: 50%;
}

</style>
