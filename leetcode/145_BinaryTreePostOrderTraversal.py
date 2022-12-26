# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # self.visited = 0
        # self.left_tag = False


class Solution:
    def __init__(self):
        self.res = []

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     l = []
    #     if not root:
    #         return l
    #     l += self.inorderTraversal(root.left)
    #     l.append(root.val)
    #     l += self.inorderTraversal(root.right)
    #     return l
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     l = []
    #     stack = []
    #     if root is None:
    #         return []
    #     stack.append(root)
    #     while root or stack:
    #         while root and not root.visited:
    #             root.visited = 1
    #             if root.right:
    #                 stack.append(root.right)
    #             if root.left_tag:
    #                 stack.append(root)
    #             if root.left:
    #                 root.left.left_tag = True
    #                 root = root.left
    #             else:
    #                 root = root.right
    #         if root and root.visited:
    #             l.append(root.val)
    #         if stack:
    #             root = stack.pop()
    #         else:
    #             root = None
    #     return l
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     l = []
    #     stack = []
    #     if root is None:
    #         return []
    #     while root or stack:
    #         while root:
    #             l.append(root.val)
    #             stack.append(root)
    #             root = root.right
    #         if stack:
    #             root = stack.pop()
    #             root = root.left
    #     return l[::-1]

    # 非递归第二版
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        while stack:
            root = stack.pop()
            self.res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return self.res[::-1]
