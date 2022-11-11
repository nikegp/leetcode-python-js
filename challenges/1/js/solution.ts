import { expect } from "../../util";

const f = (nums: number[], target: number): number[] => {
  const existingNums = new Map()

  for(let i = 0; i < nums.length; i ++) {
        if(existingNums.has(target - nums[i])) {
            return [existingNums.get(target - nums[i]), i];
        } else {
            existingNums.set(nums[i], i);
        }
    }
	return [];
};

expect(f([2, 7, 11, 15], 9), [0, 1])
expect(f([3, 2, 4], 6), [1, 2])
expect(f([3, 3], 6), [0, 1])
