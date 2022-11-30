#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for column in range(n)] for row in range(n)]

        boundaries = {
            "min_row": 0,
            "min_column": 0,
            "max_row": n - 1,
            "max_column": n - 1,
        }

        current = 1
        while True:
            # forward direction
            for column in range(boundaries["min_column"], boundaries["max_column"] + 1):
                matrix[boundaries["min_row"]][column] = current
                current += 1

            boundaries["min_row"] += 1
            if boundaries["min_row"] > boundaries["max_row"]:
                break

            # top to bottom
            for row in range(boundaries["min_row"], boundaries["max_row"] + 1):
                matrix[row][boundaries["max_column"]] = current
                current += 1

            boundaries["max_column"] -= 1
            if boundaries["max_column"] < boundaries["min_column"]:
                break

            # right to left
            for column in range(boundaries["max_column"], boundaries["min_column"] - 1, -1):
                matrix[boundaries["max_row"]][column] = current
                current += 1

            boundaries["max_row"] -= 1
            if boundaries["max_row"] < boundaries["min_row"]:
                break

            # bottom to top
            for row in range(boundaries["max_row"], boundaries["min_row"] - 1, -1):
                matrix[row][boundaries["min_column"]] = current
                current += 1

            boundaries["min_column"] += 1
            if boundaries["min_column"] > boundaries["max_column"]:
                break

        return matrix


if __name__ == "__main__":
    obj = Solution()
    expect(
        obj.generateMatrix(3),
        [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ],
    )
