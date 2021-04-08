# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # self.visited = 0
        # self.left_tag = False


class Solution:
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        stack = []
        if root is None:
            return []
        while root or stack:
            while root:
                l.append(root.val)
                stack.append(root)
                root = root.right
            if stack:
                root = stack.pop()
                root = root.left
        return l[::-1]


if __name__ == '__main__':
    tree_1 = TreeNode(1)
    tree_2 = TreeNode(2)
    tree_3 = TreeNode(3)
    tree_4 = TreeNode(4)
    tree_5 = TreeNode(5)
    tree_6 = TreeNode(6)
    tree_7 = TreeNode(7)
    tree_8 = TreeNode(8)

    tree_1.left = tree_2
    tree_1.right = tree_3
    tree_2.left = tree_4
    tree_2.right = tree_5
    tree_5.left = tree_7
    tree_5.right = tree_8
    tree_3.left = tree_6
    print(Solution().postorderTraversal(tree_1))

