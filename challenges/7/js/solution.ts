import { expect } from "../../util";

const reverse = (x: number): number => {
  const maxInt = 2147483647;
  const maxIntStr = maxInt.toString();

  let s = x.toString();
  let signMultiplier = 1;
  if (s[0] === "-") {
    signMultiplier = -1;
    s = s.slice(1);
  }

  const reversedString = [...s].reverse().join("");
  if (reversedString.length == maxIntStr.length) {
    if (reversedString > maxIntStr) return 0;
  }

  return signMultiplier * parseInt(reversedString);
};

expect(reverse(123), 321);
expect(reverse(-123), -321);
expect(reverse(120), 21);
expect(reverse(-2147483646), 0);
