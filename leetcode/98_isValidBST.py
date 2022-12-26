# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root:
    #         return False
    #     res, _, _ = self.isValidBSTWithRange(root)
    #
    #     return res
    #
    # def isValidBSTWithRange(self, root: TreeNode) -> Tuple[bool, int, int]:
    #     if root.left:
    #         left_child_is_valid, max_in_left_child, min_in_left_child = self.isValidBSTWithRange(root.left)
    #     else:
    #         left_child_is_valid = True
    #         min_in_left_child = root.val
    #         max_in_left_child = root.val
    #
    #     if root.right:
    #         right_child_is_valid, max_in_right_child, min_in_right_child = self.isValidBSTWithRange(root.right)
    #     else:
    #         right_child_is_valid = True
    #         min_in_right_child = root.val
    #         max_in_right_child = root.val
    #
    #     res = True
    #     res = res & (left_child_is_valid and right_child_is_valid)
    #
    #     if root.right:
    #         if min_in_right_child <= root.val:
    #             res = res & False
    #         if root.val >= root.right.val:
    #             res = res & False
    #     if root.left:
    #         if max_in_left_child >= root.val:
    #             res = res & False
    #         if root.val <= root.left.val:
    #             res = res & False
    #
    #     return res, max(max_in_left_child, max_in_right_child), min(min_in_right_child, min_in_left_child)

    # 清晰的解
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.isValidBSTWithRange(root, float("-inf"), float("+inf"))

    def isValidBSTWithRange(self, root: TreeNode, min: float, max: float) -> bool:
        if not root:
            return True
        val = float(root.val)
        return (
            (val > min)
            & (val < max)
            & self.isValidBSTWithRange(root.left, min, val)
            & self.isValidBSTWithRange(root.right, val, max)
        )


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        l = self.pre_order(root)
        for i, node in enumerate(l):
            if i - 1 >= 0 and l[i - 1] >= l[i]:
                return False
        return True

    def pre_order(self, root: TreeNode) -> list:
        if not root:
            return []
        l = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                l.append(root.val)
                root = root.right
        return l
