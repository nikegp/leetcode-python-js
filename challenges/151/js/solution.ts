import { expect } from "../../util";

const reverseWords = (s: string): string => {
  return s
    .split(" ")
    .filter((word) => word)
    .reverse()
    .join(" ");
};

expect(reverseWords("  hello world  "), "world hello");
expect(reverseWords("a good   example"), "example good a");
