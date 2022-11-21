def expect(a, b):
    quote_a = "'" if isinstance(a, str) else ""
    quote_b = "'" if isinstance(b, str) else ""

    if type(a) != type(b):
        print(f"TYPES MISSMATCH! Received {type(a)} while expecting {type(b)}")

    if a == b:
        print(f"Passed: {quote_a}{a}{quote_a} == {quote_b}{b}{quote_b}")
    else:
        print(f"Failed: got {quote_a}{a}{quote_a} while expecting {quote_b}{b}{quote_b}")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
