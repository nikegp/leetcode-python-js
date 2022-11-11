import { expect } from "../../util";

const f = (s: string): string => {
  if (!s.length) {
    return s;
  }

  const stack = [];
  for (let i = 0; i < s.length; i++) {
    const topChar = stack.length ? stack[stack.length - 1] : "";
    if (
      topChar &&
      topChar !== s[i] &&
      topChar.toLowerCase() === s[i].toLowerCase()
    ) {
      stack.pop();
    } else {
      stack.push(s.charAt(i));
    }
  }

  return stack.join("");
};

expect(f(""), "");
expect(f("leEeetcode"), "leetcode");
expect(f("abBAcC"), "");
