#!/usr/bin/env python
from collections import deque

from challenges.utils import expect

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        queue = deque([node])
        cloned = {node.val: Node(node.val)}

        while queue:
            item = queue.popleft()
            item_copy = cloned[item.val]

            for neighbor in item.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                item_copy.neighbors.append(cloned[neighbor.val])

        return cloned[node.val]


if __name__ == "__main__":
    obj = Solution()
    # expect(obj.fun(), EXPECTED_OUTPUT)
