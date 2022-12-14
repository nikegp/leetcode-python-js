#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest_palindrome_boundaries = (0, 0)
        for i in range(len(s) - 1):
            left, right = self.get_max_palindrome_boundaries(s, i, i)
            if right - left > longest_palindrome_boundaries[1] - longest_palindrome_boundaries[0]:
                longest_palindrome_boundaries = (left, right)

            left, right = self.get_max_palindrome_boundaries(s, i, i + 1)
            if right - left > longest_palindrome_boundaries[1] - longest_palindrome_boundaries[0]:
                longest_palindrome_boundaries = (left, right)

        return s[longest_palindrome_boundaries[0] : longest_palindrome_boundaries[1] + 1]

    def get_max_palindrome_boundaries(self, s: str, left: int = 0, right: int = 0) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1


if __name__ == "__main__":
    obj = Solution()

    # expect(obj.get_max_palindrome_boundaries("bb", 0, 0), (0, 0))
    # expect(obj.get_max_palindrome_boundaries("bb", 0, 1), (0, 1))
    # expect(obj.get_max_palindrome_boundaries("cbbd", 1, 1), (1, 1))
    # expect(obj.get_max_palindrome_boundaries("cbbd", 1, 2), (1, 2))
    # expect(obj.get_max_palindrome_boundaries("bbbad", 0, 0), (0, 0))
    # expect(obj.get_max_palindrome_boundaries("bbad", 0, 1), (0, 1))
    # expect(obj.get_max_palindrome_boundaries("bbbad", 1, 1), (0, 2))
    # expect(obj.get_max_palindrome_boundaries("asabba", 3, 4), (2, 5))
    # expect(obj.get_max_palindrome_boundaries("asabba", 3, 3), (3, 3))
    # expect(obj.get_max_palindrome_boundaries("asaba", 3, 3), (2, 4))
    # expect(obj.get_max_palindrome_boundaries("asaaaba", 3, 3), (2, 4))

    expect(obj.longestPalindrome("cbbd"), "bb")
    expect(obj.longestPalindrome("bb"), "bb")
    expect(obj.longestPalindrome("babad"), "bab")
    expect(obj.longestPalindrome("cbbdjhf"), "bb")
    expect(obj.longestPalindrome("aaavbn"), "aaa")
    expect(obj.longestPalindrome("vbnaaa"), "aaa")
    expect(obj.longestPalindrome("vbnaaaa"), "aaaa")
    expect(obj.longestPalindrome("aaaavbn"), "aaaa")
