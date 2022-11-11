import itertools
import operator
from collections import Counter, defaultdict
from typing import List


def expect(a, b):
    if a == b:
        print("Passed: ", a, " == ", b)
    else:
        print("Failed: got ", a, " while expecting ", b)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def f2(numbers: list[int], queries: list[list[int]]) -> list[int]:
    if not numbers or not queries:
        return []

    return [
        sum([number or query[2] for number in numbers[query[0] - 1 : query[1]]])
        for query in queries
    ]


def f3(numbers: list[int], queries: list[list[int]]) -> list[int]:
    intervals = dict()
    for query in queries:
        key = f"{query[0]}:{query[1]}"
        if key in intervals:
            continue

        zeros_cnt = 0
        s = 0
        for number in numbers[query[0] - 1 : query[1]]:
            if not number:
                zeros_cnt += 1
            else:
                s += number
        intervals[key] = (s, zeros_cnt)

    results = []
    for query in queries:
        key = f"{query[0]}:{query[1]}"
        results.append(intervals[key][0] + intervals[key][1] * query[2])

    return results


def f1(numbers: list[int], queries: list[list[int]]) -> list[int]:
    result = []
    zero_cnt = 0
    zero_cnt_array = [0] * len(numbers)
    sub_sequence_sum = [0] * len(numbers)

    for i in range(0, len(numbers)):
        if numbers[i] == 0:
            zero_cnt += 1
            zero_cnt_array[i] = zero_cnt
        else:
            zero_cnt_array[i] = zero_cnt
        sub_sequence_sum[i] = sub_sequence_sum[i - 1] + numbers[i]

    for query in queries:
        s = sub_sequence_sum[query[1] - 1] - (
            0 if (query[0] - 2 < 0) else sub_sequence_sum[query[0] - 2]
        )
        s = (
            s
            + (
                zero_cnt_array[query[1] - 1]
                - (0 if (query[0] - 2 < 0) else zero_cnt_array[query[0] - 2])
            )
            * query[2]
        )
        result.append(s)

    return result


def f10(files: list[int], numCores: int, limit: int) -> int:
    files_sorted = sorted(files, reverse=True)
    files_to_parallelize = limit
    execution_time = 0
    for lines_count in files_sorted:
        if files_to_parallelize and lines_count % numCores == 0:
            execution_time += lines_count // numCores
            files_to_parallelize -= 1
        else:
            execution_time += lines_count

    return execution_time


if __name__ == "__main__":
    pass
    expect(f1([5, 10, 10], [[1, 2, 5]] * 1000), [15] * 1000)
    # expect(f1(["ab", "", "c"], ["a", "bc"]), True)
