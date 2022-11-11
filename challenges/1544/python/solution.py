#!/usr/bin/env python

from challenges.utils import expect


def f(s: str) -> str:
    if not s:
        return s

    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
            stack.pop(-1)
        else:
            stack.append(s[i])

    return "".join(stack)


if __name__ == "__main__":
    expect(f(""), "")
    expect(f("leEeetcode"), "leetcode")
    expect(f("abBAcC"), "")
