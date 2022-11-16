/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

export const countNodes = (root, l = 1, r = 1) => {
  if (!root) {
    return 0;
  }

  let left = root,
    right = root;

  while ((left = left.left)) {
    l += 1;
  }
  while ((right = right.right)) {
    r += 1;
  }

  if (l == r) {
    return Math.pow(2, l) - 1;
  }

  return 1 + countNodes(root.left) + countNodes(root.right);
};
