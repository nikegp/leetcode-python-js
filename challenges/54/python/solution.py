#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        boundaries = {
            "min_row": 0,
            "min_column": 0,
            "max_row": len(matrix) - 1,
            "max_column": len(matrix[0]) - 1,
        }
        res = []
        while True:
            # forward direction
            for column in range(boundaries["min_column"], boundaries["max_column"] + 1):
                yield matrix[boundaries["min_row"]][column]

            boundaries["min_row"] += 1
            if boundaries["min_row"] > boundaries["max_row"]:
                break

            # top to bottom
            for row in range(boundaries["min_row"], boundaries["max_row"] + 1):
                yield matrix[row][boundaries["max_column"]]

            boundaries["max_column"] -= 1
            if boundaries["max_column"] < boundaries["min_column"]:
                break

            # right to left
            for column in range(boundaries["max_column"], boundaries["min_column"] - 1, -1):
                yield matrix[boundaries["max_row"]][column]

            boundaries["max_row"] -= 1
            if boundaries["max_row"] < boundaries["min_row"]:
                break

            # bottom to top
            for row in range(boundaries["max_row"], boundaries["min_row"] - 1, -1):
                yield matrix[row][boundaries["min_column"]]

            boundaries["min_column"] += 1
            if boundaries["min_column"] > boundaries["max_column"]:
                break

        return res


if __name__ == "__main__":
    obj = Solution()
    expect(
        list(
            obj.spiralOrder(
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                ]
            )
        ),
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    )
    expect(
        list(
            obj.spiralOrder(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                ]
            )
        ),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    )
