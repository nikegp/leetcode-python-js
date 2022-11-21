import { expect } from "../../util";

const longestPalindrome = (s: string): string => {
  let left, longestPalindromeBoundaries, right;

  if (s.length <= 1) {
    return s;
  }

  longestPalindromeBoundaries = [0, 0];

  for (let i = 0; i < s.length - 1; i += 1) {
    [left, right] = getMaxPalindromeBoundaries(s, i, i);

    if (right - left > longestPalindromeBoundaries[1] - longestPalindromeBoundaries[0]) {
      longestPalindromeBoundaries = [left, right];
    }

    [left, right] = getMaxPalindromeBoundaries(s, i, i + 1);

    if (right - left > longestPalindromeBoundaries[1] - longestPalindromeBoundaries[0]) {
      longestPalindromeBoundaries = [left, right];
    }
  }

  return s.slice(longestPalindromeBoundaries[0], longestPalindromeBoundaries[1] + 1);
};

const getMaxPalindromeBoundaries = (s: string, left = 0, right = 0): [number, number] => {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    left -= 1;
    right += 1;
  }

  return [left + 1, right - 1];
};

expect(longestPalindrome("cbbd"), "bb");
expect(longestPalindrome("bb"), "bb");
expect(longestPalindrome("babad"), "bab");
expect(longestPalindrome("cbbdjhf"), "bb");
expect(longestPalindrome("aaavbn"), "aaa");
expect(longestPalindrome("vbnaaa"), "aaa");
expect(longestPalindrome("vbnaaaa"), "aaaa");
expect(longestPalindrome("aaaavbn"), "aaaa");
