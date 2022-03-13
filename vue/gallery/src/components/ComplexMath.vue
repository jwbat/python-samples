<template>
  <div class="container">
    <p>{{ s1 }}</p>
    <p>{{ s2 }}</p>
    <p>{{ s3 }}</p>
    <p><span class="conjugate">{{ s4a }}</span>{{ s4b }}</p>
    <p>{{ s5 }}</p>
  </div> 
</template>

<script>
// import { ref } from 'vue';
// import { gsap } from 'gsap';

import { sqrt, e, round, pow, conj, complex } from 'mathjs';
// pi, 
export default {
  setup() {
    const imaginary = sqrt(-4).toString();
    const s1 = `sqrt(-4) = ${ imaginary }`;
    const s2 = `9 ^ 2 = ${ pow(9, 2) }`;
    const s3 = `e = ${ round(e, 5) }`;

    const s4a = `${ complex(2, 3) }`;
    const s4b = ` = ${ conj(complex(2, 3)) }`;



    const c = complex(3, 4);
    const radius = c.abs();
    const theta = round(c.arg(), 5);

    const s5 = `${ c } = (${ radius }, ${ theta })`;

    return { s1, s2, s3, s4a, s4b, s5 };
  }
}
</script>

<style scoped>
.container {
  background: #bdc99f;
  height: 100vh;
  width: 100vw;
  padding-top: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

p {
  margin-top: 1rem;
  color: black;
  font-size: 1.4rem;
  font-weight: bold;
  letter-spacing: 3px;
}

.conjugate {
  text-decoration: overline;
}
</style>
