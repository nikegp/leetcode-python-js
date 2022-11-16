#!/usr/bin/env python


class Solution:
    def countNodes(self, root, l=1, r=1):

        if not root:
            return 0

        left = right = root
        while left := left.left:
            l += 1
        while right := right.right:
            r += 1

        if l == r:
            return 2**l - 1  # if it's a full tree, its size is known

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    pass
