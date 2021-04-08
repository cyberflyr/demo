# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     l = []
    #     if not root:
    #         return l
    #     l += self.inorderTraversal(root.left)
    #     l.append(root.val)
    #     l += self.inorderTraversal(root.right)
    #     return l
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        stack = []
        if root is None:
            return []
        while root or stack:
            while root:
                l.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                root = root.right
        return l


