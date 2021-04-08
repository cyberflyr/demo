# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        all_, level_ = [], []
        sequence = []
        if not root:
            return []
        sequence.append(root)
        next_level_count = 0
        current_level_count = 1
        passed = 0
        while passed <= len(sequence):
            if root.left:
                sequence.append(root.left)
                next_level_count += 1
            if root.right:
                sequence.append(root.right)
                next_level_count += 1
            level_.append(root.val)
            current_level_count -= 1
            if current_level_count == 0:
                current_level_count = next_level_count
                next_level_count = 0
                all_.append(level_)
                level_ = list()
            passed += 1
            if passed < len(sequence):
                root = sequence[passed]
        return all_


if __name__ == '__main__':
    tree_1 = TreeNode(3)
    tree_2 = TreeNode(9)
    tree_3 = TreeNode(20)
    tree_4 = TreeNode(15)
    tree_5 = TreeNode(7)

    tree_1.left = tree_2
    tree_1.right = tree_3
    tree_3.left = tree_4
    tree_3.right = tree_5
    print(Solution().levelOrder(tree_1))