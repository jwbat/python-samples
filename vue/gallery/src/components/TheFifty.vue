<template>
  <div class="top">
    <div class="container">
      <div
        v-for="num in 50"
        :key="num"
        class="item1"
      ></div> 
    </div> 
    <div class="container">
      <div
        v-for="num in 50"
        :key="num"
        class="item2"
      ></div>
    </div> 
  </div> 
</template>

<script>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

import { rand } from '../util/funcs.js';

export default {
  setup() {

    onMounted(play);
    
    function play() {
      const tl = gsap.timeline();
      // 1
      tl.from('.item1', {
        duration: 2,
        opacity: 0,
        scale: 0,
        y: -100,
        ease: 'power1.inOut',
        stagger: {
          each: 0.1,
          from: 'edges'
        }
      })
      tl.to('.item1', {
        duration: 2,
        opacity: 0.9,
        backgroundColor: () => ['crimson', 'purple', 'maroon'][rand(3)()],
      }, '<')
      // 2
      tl.to('.item2', {
        duration: 3,
        backgroundColor: 'black',
        opacity: 0.9,
        y: 'random(-200, 200)',
        height: '30%',
        ease: 'power2.inOut',
        stagger: {
          each: 0.1,
          from: 'center'
        }
      })
      // 3
      tl.to('.item1', {
        delay: 2,
        duration: 1,
        opacity: 1,
        backgroundImage: 'linear-gradient(black, red)',
        scale: 0.5,
        ease: 'power1.inOut',
        stagger: {
          each: 0.05,
          from: 'center'
        }
      })
      // 4
      tl.to('.item2', {
        delay: 2,
        duration: 3,
        backgroundColor: 'white',
        opacity: 0.5,
        height: '10%',
        y: () => ['-300', '200', '50'][rand(3)()],
        ease: 'power1.inOut',
        stagger: {
          each: 0.1,
          from: 'edges'
        }
      })
      // 5
      tl.to('.item1', {
        duration: 1,
        backgroundImage: 'linear-gradient(black, red, blue)',
        scale: 0.5,
        ease: 'power1.inOut',
        stagger: {
          each: 0.05,
          from: 'center'
        }
      })
      // 6
      tl.to('.item2', {
        duration: 3,
        backgroundColor: 'black',
        opacity: 0.6,
        y: () => ['-80%', '90', '10%', '-30'][rand(4)()]
      }, '<')
      // 7
      tl.to('.item1', {
        delay: 2,
        duration: 0.5,
        backgroundColor: 'bisque',
        scale: 0.9,
        borderRadius: '50%',
        ease: 'power3.inOut',
        y: () => ['-40vh', '-10vh', '12vh', '22vh', '30vh'][rand(5)()],
        width: 'random(5, 50)',
        height: 'random(10, 200)',
        stagger: {
          each: 0.1,
          from: 'edges'
        }
      })
      // 8
      tl.to('.item2', {
        duration: 0.5,
        scale: 1,
        borderRadius: '50%',
        opacity: () => [0, 0.4, 0.2][rand(3)()],
        backgroundColor: () => ['pink', 'white'][rand(2)()],
        ease: 'power3.inOut',
        stagger: {
          each: 0.1,
          from: 'center'
        }
      }, '<')
      // 9
      tl.to('.item2', {
        duration: 3,
        x: () => ['-100vw', '100vw'][rand(2)()],
//         y: () => ['-100vh', '100vh'][rand(2)()],
        opacity: 0.1,
        ease: 'power2',
        stagger: {
          each: 0.2,
          from: 'right'
        }
      }, '<')
    }
  }
}
</script>

<style scoped>
.top {
  position: relative;
  height: 100%;
  width: 100%;
}
.container {
  position: absolute;
  top: 0;
  left: 0;
  background: black;
  padding: 2rem; 
  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-columns: repeat(50, 1fr);
}

.item1 {
  border: 2px solid black;
  background: red;
  z-index: 5;
}

.item2 {
  opacity: 0;
  height: 100%;
  background: blue;
  align-self: center;
  z-index: 10;
}
</style>

