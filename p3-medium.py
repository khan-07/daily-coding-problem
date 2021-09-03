# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# Made a mess , will come back to this
global serialized_tree
serialized_tree = ''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node,serialized_tree):
    # let's serialize it using dfs

    if node:
        serialized_tree += node.val + "-"
    if node.left:
        serialized_tree += serialize(node.left,'')
    if node.right:
        serialized_tree += serialize(node.right,'')

    return serialized_tree


def deserialize(serialized_tree):
    serialized_tree =  serialized_tree.split("-")
    node_previous  = None
    node_current = None
    for idx,val in enumerate(serialized_tree):
        if(idx == 0):
            node_current = Node(val)
        elif (idx == len(serialized_tree) -1):
            node_current = node_current
        else:
            if (node_previous.val == 'left')
            node_current = Node(val)
            node_previous.left
        node_previous = node_current



node = Node('root', Node('left', Node('left.left')), Node('right'))
if(node.left.right):
    print(node.left)
    print(node.right)
print(serialize(node,serialized_tree).split("-"))
# assert deserialize(serialize(node)).left.left.val == 'left.left'