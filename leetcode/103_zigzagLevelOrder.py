# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        current_nodes = [root]
        next_level_nodes = []
        res = []
        level_res = []
        while current_nodes:
            node = current_nodes.pop(0)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

            level_res.append(node.val)

            if not current_nodes:
                if level % 2 == 0:
                    res.append(level_res)
                else:
                    res.append(level_res[::-1])
                level += 1
                current_nodes, next_level_nodes = next_level_nodes, []
                level_res = []
        return res
