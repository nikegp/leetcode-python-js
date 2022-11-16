#!/usr/bin/env python
from challenges.utils import expect


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left, right = 0, 0
        positions = {s[left]: 0}
        max_seen_length = 0
        while right < len(s) - 1:
            right += 1
            if s[right] in positions:
                left = max(left, positions[s[right]] + 1)

            positions[s[right]] = right
            max_seen_length = max(max_seen_length, right - left + 1)

        return max_seen_length


if __name__ == "__main__":
    obj = Solution()
    expect(obj.lengthOfLongestSubstring(""), 0)
    expect(obj.lengthOfLongestSubstring("a"), 1)
    expect(obj.lengthOfLongestSubstring("abcba"), 3)
    expect(obj.lengthOfLongestSubstring("abcabcbb"), 3)
    expect(obj.lengthOfLongestSubstring("bbbbb"), 1)
    expect(obj.lengthOfLongestSubstring("pwwkew"), 3)
