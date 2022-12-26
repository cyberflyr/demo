class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_z_path(root: TreeNode):
    level_members = level_order(root)
    res = []
    for k, v in level_members.items():
        temp = []
        if k % 2 == 0:
            while v:
                temp.append(v.pop(-1).val)
        else:
            while v:
                temp.append(v.pop(0).val)
        res.append(temp)
    return res


def level_order(root: TreeNode):
    queue = [root]
    level_members = {1: []}
    level = 1
    cur_num = 1
    next_num = 0
    while queue:
        if level not in level_members:
            level_members[level] = []
        node = queue.pop(0)
        level_members[level].append(node)
        if node.left:
            next_num += 1
            queue.append(node.left)
        if node.right:
            next_num += 1
            queue.append(node.right)
        cur_num -= 1
        if cur_num == 0:
            cur_num, next_num = next_num, 0
            level += 1
    return level_members


# [4, 6, 2, 1, 3, 5, 7]


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)

    root = t4
    t4.left = t2
    t2.left = t1
    t2.right = t3
    t4.right = t6
    t6.left = t5
    t6.right = t7
    print(print_z_path(root))
