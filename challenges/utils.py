def expect(a, b):
    if type(a) != type(b):
        print(f"TYPES MISSMATCH! Received {type(a)} while expecting {type(b)}")
    elif a == b:
        print(f"Passed: '{a}' == '{b}'")
    else:
        print(f"Failed: got '{a}' while expecting '{b}'")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
