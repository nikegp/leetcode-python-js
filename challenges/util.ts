export const expect = (a: any, b: any) => {
  if (a === b) {
    console.log(`PASSED ${a} === ${b}`);
  } else {
    console.log(`Mismatch! ${a} !== ${b}`);
  }
};