import { expect } from "../../util";

const isUgly = (n: number): boolean => {
  if (n === 0) return false;

  const primeFactors = [2, 3, 5];
  for (const primeFactor of primeFactors) {
    while (n % primeFactor === 0) n /= primeFactor;
  }

  return n === 1;
};

expect(isUgly(5), true);
expect(isUgly(6), true);
expect(isUgly(1), true);
expect(isUgly(14), false);
