#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def computeArea(
        self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int
    ) -> int:
        area_of_a = (ay2 - ay1) * (ax2 - ax1)
        area_of_b = (by2 - by1) * (bx2 - bx1)

        # calculate x overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left

        # calculate y overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        overlap_area = 0
        if x_overlap > 0 and y_overlap > 0:
            overlap_area = x_overlap * y_overlap

        return area_of_a + area_of_b - overlap_area


if __name__ == "__main__":
    obj = Solution()
    expect(obj.computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2), 45)
