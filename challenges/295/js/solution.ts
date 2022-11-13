// has to be var to be compatible with LeetCode
import { expect, zip } from "../../util";

class MedianFinder {
  sortedNums: number[];

  constructor() {
    this.sortedNums = [];
  }

  findIndex(num: number): number {
    let [left, right] = [0, this.sortedNums.length - 1];

    while (left <= right) {
      if (this.sortedNums[left] >= num) {
        return left;
      }
      if (this.sortedNums[right] <= num) {
        return right + 1;
      }

      const middleIndex = Math.floor((left + right) / 2);
      const middleNum = this.sortedNums[middleIndex];
      if (middleNum === num) {
        return middleIndex;
      }

      //[2, 5, 10]; 3
      if (middleNum > num) {
        right = middleIndex - 1;
      } else {
        left = middleIndex + 1;
      }
    }

    return 0;
  }

  findMedian(): number | null {
    const length = this.sortedNums.length;
    if (!length) {
      return null;
    }

    const medianIndex = Math.floor((length - 1) / 2);
    if (length % 2 === 0) {
      return (
        (this.sortedNums[medianIndex] + this.sortedNums[medianIndex + 1]) / 2
      );
    } else {
      return this.sortedNums[medianIndex];
    }
  }

  addNum(num: number): null {
    if (!this.sortedNums.length) {
      this.sortedNums = [num];
    } else {
      this.sortedNums.splice(this.findIndex(num), 0, num);
    }
    return null;
  }
}

const obj: { [key: string]: any } = new MedianFinder();
for (const [method, params, output] of zip([
  ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
  [[], [1], [2], [], [3], []],
  [null, null, null, 1.5, null, 2.0],
])) {
  if (method === "MedianFinder") {
    continue;
  }
  expect(obj[method as string](...params), output);
}
