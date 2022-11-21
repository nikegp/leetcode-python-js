#!/usr/bin/env python
from functools import cache
from typing import List

from challenges.utils import expect


class Solution:
    def minDifficulty(self, job_difficulty: List[int], d: int) -> int:
        @cache
        def get_min_difficulty(task_index: int, days: int) -> int:
            if days == 1:
                return max(job_difficulty[task_index:])

            # task_index == 0
            # [1, 2, 3, 4] tasks
            # 2 days => loop over [1, 2, 3] tasks
            min_difficulty_seen = float("+inf")
            current_day_complexity = float("-inf")
            for i in range(task_index, len(job_difficulty) - days + 1):
                current_day_complexity = max(current_day_complexity, job_difficulty[i])
                min_difficulty_seen = min(
                    min_difficulty_seen,
                    current_day_complexity + get_min_difficulty(i + 1, days - 1),
                )
            return min_difficulty_seen

        return get_min_difficulty(0, d) if len(job_difficulty) >= d else -1


if __name__ == "__main__":
    obj = Solution()
    expect(obj.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6), 843)
    expect(obj.minDifficulty([1, 1, 1], 3), 3)
    expect(obj.minDifficulty([6, 5, 4, 3, 2, 1], 2), 7)
    expect(
        obj.minDifficulty(
            [186, 398, 479, 206, 885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360], 4
        ),
        1803,
    )
    expect(obj.minDifficulty([6], 2), -1)
