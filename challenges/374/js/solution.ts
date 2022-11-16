/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

export const guess = (num: number): number => 1;

const guessNumber = (n: number): number => {
  let left = 1,
    right = n;
  while (true) {
    const middle = Math.floor((left + right) / 2);
    const guessResult = guess(middle);
    if (guessResult === 1) {
      left = middle + 1;
    } else if (guessResult === -1) {
      right = middle - 1;
    } else {
      return middle;
    }
  }
};
