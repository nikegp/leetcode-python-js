#!/usr/bin/env python
from challenges.utils import expect


def reverse_words(s: str) -> str:
    if not s:
        return s

    return " ".join([word for word in reversed(s.split(" ")) if word])


if __name__ == "__main__":
    expect(reverse_words("  hello world  "), "world hello")
    expect(reverse_words("a good   example"), "example good a")
