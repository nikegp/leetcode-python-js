#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        prime_factors = [2, 3, 5]
        for prime_factor in prime_factors:
            while n % prime_factor == 0:
                n /= prime_factor

        return n == 1


if __name__ == "__main__":
    obj = Solution()
    expect(obj.isUgly(5), True)
    expect(obj.isUgly(6), True)
    expect(obj.isUgly(1), True)
    expect(obj.isUgly(14), False)
