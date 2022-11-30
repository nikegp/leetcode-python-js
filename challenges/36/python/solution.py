#!/usr/bin/env python
from collections import defaultdict
from typing import List

from challenges.utils import expect


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_cnt = len(board)
        columns_cnt = len(board[0])

        unique_row_elements = defaultdict(set)
        unique_column_elements = defaultdict(set)
        unique_block_elements = defaultdict(set)

        for row in range(rows_cnt):
            for column in range(columns_cnt):
                element = board[row][column]
                if element == ".":
                    continue
                # 0 1 2
                # 3 4 5
                # 6 7 8
                block_index = row // 3 * 3 + column // 3
                if (
                    element in unique_row_elements[row]
                    or element in unique_column_elements[column]
                    or element in unique_block_elements[block_index]
                ):
                    return False

                unique_row_elements[row].add(element)
                unique_column_elements[column].add(element)
                unique_block_elements[block_index].add(element)

        return True


if __name__ == "__main__":
    obj = Solution()
    expect(
        obj.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
        True,
    )

    expect(
        obj.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
        False,
    )
