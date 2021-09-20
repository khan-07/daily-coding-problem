# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# Three structures come to mind 1) Array (S=0(N),T=0(1))2) Linked List(S=0(N),T=0(N)) 3) Hash Map (S=0(N),T=0(1))

# Implemented it with linked list but array can be used as well as one of the operations will be always O(n)
class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val


class Log:
    def __init__(self, size=1):
        self.order_array = [-1] * size
        self.head = None
        self.max_size = size
        self.size = 0
        self.tail = self.head

    def record(self, order_id):

        if self.size < self.max_size:
            if not self.head:
                self.head = Node(order_id)
                self.tail = self.head
                self.size += self.size
            else:
                node = Node(order_id)
                temp = self.tail
                temp.next = node
                self.tail = node
                self.size = self.size + 1
        else:
            node = Node(order_id)
            temp = self.tail
            temp.next = node
            self.tail = node
            self.head = self.head.next

    def get_last(self, i):
        iterations = self.size - i + 1
        node = self.head
        k = 0
        while k != iterations:
            node = node.next
            k += 1

        return node.val


log = Log(size = 5)
for j in range(1,6):
    log.record(j)

print(log.get_last(2))