import { expect } from "../../util";

const computeArea = (
  ax1: number,
  ay1: number,
  ax2: number,
  ay2: number,
  bx1: number,
  by1: number,
  bx2: number,
  by2: number
): number => {
  const areaA = (ax2 - ax1) * (ay2 - ay1);
  const areaB = (bx2 - bx1) * (by2 - by1);

  const xOverlap = Math.min(ax2, bx2) - Math.max(ax1, bx1);
  const yOverlap = Math.min(ay2, by2) - Math.max(ay1, by1);
  let overlapArea = 0;
  if (xOverlap > 0 && yOverlap > 0) {
    overlapArea = xOverlap * yOverlap;
  }

  return areaA + areaB - overlapArea;
};

expect(computeArea(-3, 0, 3, 4, 0, -1, 9, 2), 45);
