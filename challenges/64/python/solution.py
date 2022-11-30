#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows_cnt = len(grid)
        columns_cnt = len(grid[0])

        for row in range(rows_cnt):
            for column in range(columns_cnt):
                if row == 0 and column == 0:
                    continue

                left_sum = float("+inf") if column == 0 else grid[row][column - 1]
                top_sum = float("+inf") if row == 0 else grid[row - 1][column]

                grid[row][column] += min(left_sum, top_sum)

        return grid[-1][-1]


if __name__ == "__main__":
    obj = Solution()
    expect(obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
    expect(obj.minPathSum([[1, 2, 3], [4, 5, 6]]), 12)
