# A unival tree (which stands for "universal value") is a tree where all
# nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Tree:
    def __init__(self, root):
        self.root = root

    def build_tree(self, elements):
        return self.root


def check_unival(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        left = check_unival(root.left)
        right = check_unival(root.right)

        if root.val == root.left.val == root.right.val:
            return 1 + left + right
        else:
            return left + right
