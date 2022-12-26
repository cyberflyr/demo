from dataclasses import dataclass


@dataclass()
class TreeNode:
    parent: None
    left: None
    right: None


def tree_minimum(t: TreeNode):
    # 迭代
    while t.left:
        t = t.left
    return t


def tree_maximum(t: TreeNode):
    # 递归
    if t is None:
        return t
    if t.right:
        return tree_maximum(t.right)
    return t


def find_tree_successor(x: TreeNode):
    if x.right:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and y.right == x:
        x = y
        y = y.parent
    return y


def find_tree_predecessor(x: TreeNode):
    if x.left:
        return tree_maximum(x.left)
    y = x.parent
    while y is not None and y.left == x:
        x = y
        y = y.parent
    return y
