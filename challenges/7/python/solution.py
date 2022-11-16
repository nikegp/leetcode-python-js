#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        max_int_str = str(max_int)

        s = str(x)
        sign_multiplier = 1
        if s[0] == "-":
            sign_multiplier = -1
            s = s[1:]

        reversed = s[::-1]
        if len(reversed) == len(max_int_str):
            if reversed > max_int_str:
                return 0

        return sign_multiplier * int(reversed)


if __name__ == "__main__":
    obj = Solution()
    expect(obj.reverse(123), 321)
    expect(obj.reverse(-123), -321)
    expect(obj.reverse(120), 21)
    expect(obj.reverse(-2147483646), 0)
