from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        mid_idx = inorder.index(root.val)
        left_root = self.buildTree(preorder[1 : mid_idx + 1], inorder[:mid_idx])
        right_root = self.buildTree(preorder[mid_idx + 1 :], inorder[mid_idx + 1 :])
        root.left = left_root
        root.right = right_root
        return root
