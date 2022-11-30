#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for _ in range(n)] for _ in range(m)]

        for row in range(1, m):
            for column in range(1, n):
                paths[row][column] = paths[row][column - 1] + paths[row - 1][column]

        return paths[-1][-1]


if __name__ == "__main__":
    obj = Solution()
    expect(obj.uniquePaths(3, 7), 28)
