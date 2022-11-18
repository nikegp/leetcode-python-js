#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(s) == 0:
            return 0

        while pos < len(s):
            current_char = s[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+":
                    state = 1
                elif current_char == "-":
                    state = 1
                    sign = -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2**31 - 1)
        value = max(-(2**31), value)

        return value


if __name__ == "__main__":
    obj = Solution()
    expect(obj.myAtoi("42"), 42)
    expect(obj.myAtoi("   -42"), -42)
    expect(obj.myAtoi("4193 with words"), 4193)
