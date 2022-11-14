import { expect } from "../../util";

const removeStones = (stones: number[][]): number => {
  const neighborsX = new Map();
  const neighborsY = new Map();

  for (const [x, y] of stones) {
    neighborsX.set(x, (neighborsX.get(x) || new Set()).add(y));
    neighborsY.set(y, (neighborsY.get(y) || new Set()).add(x));
  }

  const visitedStones = new Set();
  let linkedStoneCount = 0;

  for (const [x, y] of stones) {
    if (visitedStones.has(`${x}:${y}`)) {
      continue;
    }

    linkedStoneCount += 1;

    const queue: number[][] = [[x, y]];

    while (queue.length) {
      const [currentX, currentY] = queue.pop() || [];
      if (visitedStones.has(`${currentX}:${currentY}`)) {
        continue;
      }

      visitedStones.add(`${currentX}:${currentY}`);

      for (const neighborY of neighborsX.get(currentX)) {
        queue.push([currentX, neighborY]);
      }

      for (const neighborX of neighborsY.get(currentY)) {
        queue.push([neighborX, currentY]);
      }
    }
  }

  return stones.length - linkedStoneCount;
};

expect(
  removeStones([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 2],
    [2, 1],
    [2, 2],
  ]),
  5
);
