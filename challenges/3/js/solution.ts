import { expect } from "../../util";

export const lengthOfLongestSubstring = (s: string): number => {
  const sLength = s.length;
  if (sLength <= 1) {
    return sLength;
  }

  let left = 0,
    right = 0;
  let maxSeenLength = 0;
  const charPositions = new Map([[s[0], 0]]);
  while (right < sLength - 1) {
    right += 1;
    if (charPositions.has(s[right])) {
      left = Math.max((charPositions.get(s[right]) || 0) + 1, left);
    }
    charPositions.set(s[right], right);
    maxSeenLength = Math.max(maxSeenLength, right - left + 1);
  }

  return maxSeenLength;
};

expect(lengthOfLongestSubstring(""), 0);
expect(lengthOfLongestSubstring("a"), 1);
expect(lengthOfLongestSubstring("abcba"), 3);
expect(lengthOfLongestSubstring("abcabcbb"), 3);
expect(lengthOfLongestSubstring("bbbbb"), 1);
expect(lengthOfLongestSubstring("pwwkew"), 3);
