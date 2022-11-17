import { expect } from "../../util";

const gameOfLife = (board: number[][]) => {
  const maxX = board.length - 1;
  const maxY = board[0].length - 1;

  const getLiveNeighborsCnt = (x: number, y: number): number => {
    //     1,1 => (0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2)
    const directions = [
      [-1, -1],
      [0, -1],
      [1, -1],
      [-1, 0],
      [1, 0],
      [-1, 1],
      [0, 1],
      [1, 1],
    ];
    let liveCount = 0;
    for (const [offsetX, offsetY] of directions) {
      const newX = x + offsetX;
      const newY = y + offsetY;
      if (newX < 0 || newX > maxX) continue;
      if (newY < 0 || newY > maxY) continue;

      if (board[newX][newY] == 1 || board[newX][newY] == -1) {
        liveCount += 1;
      }
    }

    return liveCount;
  };

  for (let x = 0; x <= maxX; x++) {
    for (let y = 0; y <= maxY; y++) {
      const neighboursCnt = getLiveNeighborsCnt(x, y);
      if (board[x][y] == 0) {
        // cell is dead
        if (neighboursCnt === 3) board[x][y] += 2;
      } else {
        // cell is alive
        if (neighboursCnt < 2 || neighboursCnt > 3) board[x][y] -= 2;
      }
    }
  }

  for (let x = 0; x <= maxX; x++) {
    for (let y = 0; y <= maxY; y++) {
      board[x][y] = board[x][y] > 0 ? 1 : 0;
    }
  }
};

const board = [
  [0, 1, 0],
  [0, 0, 1],
  [1, 1, 1],
  [0, 0, 0],
];
gameOfLife(board);
expect(board, [
  [0, 0, 0],
  [1, 0, 1],
  [0, 1, 1],
  [0, 1, 0],
]);
