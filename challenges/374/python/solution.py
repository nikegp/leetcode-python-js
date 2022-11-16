#!/usr/bin/env python
from challenges.utils import expect


# A dummy placeholder just to avoid errors highlighting in the IDE
def guess(n: int) -> int:
    return n


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while True:
            middle = (left + right) // 2
            guess_result = guess(middle)
            if guess_result == -1:
                right = middle - 1
            elif guess_result == 1:
                left = middle + 1
            else:
                return middle


if __name__ == "__main__":
    pass
