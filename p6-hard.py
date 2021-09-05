# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end,
# and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and dereference_pointer
# functions that converts between nodes and memory addresses.

def dereference_pointer(address):
    if not address:
        return None
    return 1 # returns the node


def get_pointer(node):
    if not node:
        return 0
    return 1 # returns the address


def get_prev_next(prev_memory, node, is_root=False):
    if is_root:
        return dereference_pointer(node.both), dereference_pointer(None)
    else:
        return dereference_pointer(node.both ^ prev_memory), dereference_pointer(prev_memory)


class XorNode:
    def __init__(self, val, next_node, prev_node):
        self.val = val
        self.both = get_pointer(next_node) ^ get_pointer(prev_node)


class XorLinkedList:
    def __init__(self, val):
        self.root = XorNode(val, None, None)
        self.tail = self.root

    def add(self, element):
        if self.root == self.tail:

            self.tail = XorNode(element, None, self.root)
            self.tail.both = get_pointer(None) ^ get_pointer(self.root)
            self.root.both = get_pointer(self.tail) ^ get_pointer(None)

        else:
            temp = XorNode(element, None, self.tail.both)
            self.tail.both = self.tail.both ^ get_pointer(temp)
            self.tail = temp

    def get(self, element):
        next_node, prev = get_prev_next(dereference_pointer(0), self.root, True)
        current = self.root

        while True:
            if current is None:
                return -1

            if current.val == element:
                return current

            temp = next_node
            next_node, prev = get_prev_next(dereference_pointer(current), next_node)
            current = temp