#!/usr/bin/env python
from typing import List

from challenges.utils import expect


def f(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        raise Exception("Input list doesn't have enough elements")

    existing_nums = dict()

    for i in range(0, len(nums)):
        current = nums[i]
        desired = target - current
        if desired in existing_nums:
            return [existing_nums[desired], i]
        else:
            existing_nums[current] = i

    return []


if __name__ == "__main__":
    expect(f([2, 7, 11, 15], 9), [0, 1])
    expect(f([3, 2, 4], 6), [1, 2])
    expect(f([3, 3], 6), [0, 1])
