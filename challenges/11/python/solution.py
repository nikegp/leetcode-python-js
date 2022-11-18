#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    obj = Solution()
    expect(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
