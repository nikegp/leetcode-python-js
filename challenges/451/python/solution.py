#!/usr/bin/env python
from collections import Counter

from challenges.utils import expect


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join([char * cnt for char, cnt in c.most_common()])


if __name__ == "__main__":
    obj = Solution()
    expect(obj.frequencySort("tree") in ["eert", "eetr"], True)
    expect(obj.frequencySort("cccaaa") in ["cccaaa", "aaaccc"], True)
