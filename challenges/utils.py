def expect(a, b):
    if a == b:
        print("Passed: ", a, " == ", b)
    else:
        print("Failed: got ", a, " while expecting ", b)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
