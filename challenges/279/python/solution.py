#!/usr/bin/env python

from math import sqrt, floor

from challenges.utils import expect

memo = dict()


class Solution:
    def numSquares(self, n: int, depth: int = 1) -> int:
        if n in memo:
            return memo[n] + depth

        max_perfect_square_float = sqrt(n)
        max_perfect_square_int = floor(max_perfect_square_float)

        if max_perfect_square_float == max_perfect_square_int:
            return depth

        min_depth = float("+inf")
        for number in range(max_perfect_square_int, 0, -1):
            min_depth = min(min_depth, self.numSquares(n - number**2, depth + 1))

        memo[n] = min_depth - depth

        return min_depth


if __name__ == "__main__":
    obj = Solution()
    expect(obj.numSquares(4), 1)
    expect(obj.numSquares(12), 3)
    expect(obj.numSquares(13), 2)
    expect(obj.numSquares(206), 3)
