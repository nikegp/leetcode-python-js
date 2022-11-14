#!/usr/bin/env python
from collections import defaultdict, deque
from typing import List

from challenges.utils import expect


def remove_stones(stones: List[List[int]]) -> int:
    neighbors_x = defaultdict(list)
    neighbors_y = defaultdict(list)
    for x, y in stones:
        neighbors_x[x].append(y)
        neighbors_y[y].append(x)

    visited = set()
    connected_component_count = 0
    for x, y in stones:
        if (x, y) in visited:
            continue

        connected_component_count += 1
        queue = deque([(x, y)])
        while queue:
            x, y = queue.pop()
            if (x, y) in visited:
                continue

            visited.add((x, y))
            for neighbor_y in neighbors_x[x]:
                queue.append((x, neighbor_y))

            for neighbor_x in neighbors_y[y]:
                queue.append((neighbor_x, y))

    return len(stones) - connected_component_count


if __name__ == "__main__":
    expect(remove_stones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]), 5)
