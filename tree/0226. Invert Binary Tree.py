"""

Runtime: 28 ms, faster than 84.98% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.6 MB, less than 95.23% of Python3 online submissions for Invert Binary Tree.

"""

def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
