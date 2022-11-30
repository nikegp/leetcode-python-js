#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows_cnt = len(obstacleGrid)
        columns_cnt = len(obstacleGrid[0])

        paths = [[0 for _ in range(columns_cnt)] for _ in range(rows_cnt)]
        paths[0][0] = 1 if not obstacleGrid[0][0] else 0

        for row in range(rows_cnt):
            for column in range(columns_cnt):
                if obstacleGrid[row][column] == 1 or (row == 0 and column == 0):
                    continue

                left_paths = 0 if column == 0 else paths[row][column - 1]
                top_paths = 0 if row == 0 else paths[row - 1][column]

                paths[row][column] = left_paths + top_paths

        return paths[-1][-1]


if __name__ == "__main__":
    obj = Solution()
    expect(obj.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
    expect(obj.uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
    expect(obj.uniquePathsWithObstacles([[1]]), 0)
