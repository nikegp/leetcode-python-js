#!/usr/bin/env python
from typing import List

from challenges.utils import expect
from sortedcontainers import SortedList


class MedianFinderSimple:
    """
    A simple solution using SortedList container
    """

    def __init__(self):
        self.sorted_numbers = SortedList()

    def addNum(self, num: int) -> None:
        self.sorted_numbers.add(num)

    def findMedian(self) -> float:
        l = len(self.sorted_numbers)
        if l % 2 == 0:
            return (self.sorted_numbers[l // 2 - 1] + self.sorted_numbers[l // 2]) / 2
        return self.sorted_numbers[l // 2]


class MedianFinder:
    """
    Implemented using binary search. It's slower than the above but takes less memory.
    """

    ordered_numbers: List[int]

    def __init__(self):
        self.ordered_numbers = []

    def find_index(self, number):
        left, right = 0, len(self.ordered_numbers) - 1
        while left <= right:
            if self.ordered_numbers[left] >= number:
                return left
            if self.ordered_numbers[right] <= number:
                return right + 1

            middle_index = (right + left) // 2  # 1 => 0; 2 => 0; 3 => 1
            if number == self.ordered_numbers[middle_index]:
                return middle_index

            # [1, 5, 10]; 7 => 2
            # [1, 5, 10]; 0 => 0
            if self.ordered_numbers[middle_index] < number:
                left = middle_index + 1
            else:
                right = middle_index - 1

    def addNum(self, num: int) -> None:
        if not self.ordered_numbers:
            self.ordered_numbers = [num]
        else:
            self.ordered_numbers.insert(self.find_index(num), num)

    def findMedian(self) -> int | float | None:
        if not self.ordered_numbers:
            return None

        numbers_length = len(self.ordered_numbers)
        index = (numbers_length - 1) // 2
        if numbers_length % 2 == 1:
            return self.ordered_numbers[index]
        else:
            return (self.ordered_numbers[index] + self.ordered_numbers[index + 1]) / 2


if __name__ == "__main__":
    obj = MedianFinder()

    for method, param, result in zip(
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []],
        [None, None, None, 1.50000, None, 2.00000],
    ):
        if method == "MedianFinder":
            continue
        expect(getattr(obj, method)(*param), result)
