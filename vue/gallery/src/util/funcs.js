const randInt = (low, high) =>
  Math.floor(Math.random() * (high - low) + low);

const hsl = () => {
  const h = randInt(0, 360);
  const s = randInt(80, 100);
  const l = randInt(30, 100);
  return `hsl(${ h }, ${ s }%, ${ l }%)`;
};

const hsla = () => {
  const h = randInt(0, 360);
  const s = randInt(80, 100);
  const l = randInt(30, 100);
  const a = Math.random();
  return `hsl(${ h }, ${ s }%, ${ l }%, ${ a }%)`;
};

const rand = n => () => randInt(0, n);

const cycle = (n, i=-1) => () => {
  i = (i + 1) % n;
  return i;
};

export { hsl, hsla, rand, cycle, };
