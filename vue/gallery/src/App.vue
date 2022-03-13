<template>
  <component :is="currentCmp"></component> 
  <nav>
    <arrow-left class="btn left" @click="prevPage"></arrow-left> 
    <!--<re-load class="btn"></re-load> -->
    <arrow-right class="btn right" @click="nextPage"></arrow-right> 
  </nav> 
</template>

<script>
import { ref } from 'vue';

import FourBoxes from './components/FourBoxes.vue';
import TryThis from './components/TryThis.vue';
import TheFifty from './components/TheFifty.vue';
//import NestedModular from './components/NestedModular.vue';

import ArrowLeft from './assets/ArrowLeft.vue';
import ArrowRight from './assets/ArrowRight.vue';
// import ReLoad from './assets/ReLoad.vue';

export default {
  components: {
    'four-boxes': FourBoxes,
    'try-this': TryThis,
    'the-fifty': TheFifty,
    'arrow-left': ArrowLeft,
    'arrow-right': ArrowRight,
//    'nested-modular': NestedModular,
//     're-load': ReLoad,
  },
  setup() {
    const cmps = ['four-boxes', 'try-this', 'the-fifty']; // 'nested-modular', 
    const currentCmp = ref(cmps[0]);
    const getIdx = () => cmps.findIndex(el => el === currentCmp.value);
    const prevPage = () => {
      currentCmp.value = cmps[getIdx() - 1] || cmps[cmps.length - 1];
    };
    const nextPage = () => {
      currentCmp.value = cmps[getIdx() + 1] || cmps[0];
    };
    return {
      currentCmp,
      prevPage,
      nextPage,
    };
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html {
  background: black;
  height: 100vh;
  /*
  width: 100%;
   */
}

body {
  height: 100%;
  width: 100vw;
}

.btn {
  cursor: pointer;
  opacity: 0.5;
}

nav {
  position: absolute;
  bottom: 0;
  left: calc(50% - 5rem);
  background: none;
  width: 13rem;
  height: 5rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 10;
}

nav svg {
  stroke: grey;
  width: 5rem;
  height: 4rem;
}

.left, .right {
  margin-top: 1rem;
}

</style>
