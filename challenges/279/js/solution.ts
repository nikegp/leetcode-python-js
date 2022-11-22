import { expect } from "../../util";

let memo = new Map();

const numSquares = (n: number, depth: number = 1): number => {
  if (memo.has(n)) {
    return memo.get(n) + depth;
  }

  const maxPerfectSquareFloat = Math.sqrt(n);
  const maxPerfectSquareInt = Math.floor(maxPerfectSquareFloat);

  if (maxPerfectSquareFloat === maxPerfectSquareInt) {
    return depth;
  }

  let minDepth = Number.POSITIVE_INFINITY;
  for (let i = maxPerfectSquareInt; i >= 1; i--) {
    minDepth = Math.min(minDepth, numSquares(n - i ** 2, depth + 1));
  }

  memo.set(n, minDepth - depth);

  return minDepth;
};

expect(numSquares(4), 1);
expect(numSquares(12), 3);
expect(numSquares(13), 2);
expect(numSquares(206), 3);
