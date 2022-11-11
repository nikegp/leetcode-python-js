import { isEqual } from 'lodash';

export const expect = (a: any, b: any) => {
  if (isEqual(a, b)) {
    console.log(`PASSED ${a} === ${b}`);
  } else {
    console.log(`Mismatch! ${a} !== ${b}`);
  }
};