#!/usr/bin/env python
from typing import List

from challenges.utils import expect


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_x = len(board) - 1
        max_y = len(board[0]) - 1

        def get_live_neighbors_cnt(x: int, y: int) -> int:
            #       1,1 => (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)
            directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            live_count = 0
            for offset_x, offset_y in directions:
                new_x = x + offset_x
                new_y = y + offset_y
                if new_x < 0 or new_x > max_x:
                    continue
                if new_y < 0 or new_y > max_y:
                    continue

                if board[new_x][new_y] == 1 or board[new_x][new_y] == -1:
                    live_count += 1

            return live_count

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                neighbours_count = get_live_neighbors_cnt(x, y)
                if not board[x][y]:
                    # it's a dead cell
                    if neighbours_count == 3:
                        board[x][y] += 2
                else:
                    # it's alive cell
                    if neighbours_count < 2 or neighbours_count > 3:
                        board[x][y] -= 2

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                board[x][y] = 1 if board[x][y] > 0 else 0


if __name__ == "__main__":
    obj = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    obj.gameOfLife(board)
    expect(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
