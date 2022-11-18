import { expect } from "../../util";

const maxArea = (height: number[]): number => {
  let left = 0,
    right = height.length - 1;

  let resultArea = 0;
  while (left < right) {
    const area = Math.min(height[left], height[right]) * (right - left);
    resultArea = Math.max(area, resultArea);

    if (height[left] < height[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }
  return resultArea;
};

expect(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
