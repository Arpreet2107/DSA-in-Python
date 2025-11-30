# file: queue_linkedlist.py

class QNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    """
    FIFO queue using a singly linked list.
    Keep references to head (front) and tail (back).
    Enqueue at tail, dequeue from head; both O(1).
    """

    def __init__(self):
        self.head = None   # front of queue
        self.tail = None   # back of queue
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        node = QNode(value)
        if self.tail:
            # append after tail
            self.tail.next = node
        self.tail = node
        if not self.head:
            # first element inserted -> head must point to it
            self.head = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        node = self.head
        self.head = node.next
        if not self.head:
            # queue became empty -> tail must be None
            self.tail = None
        node.next = None  # optional: help GC
        self._size -= 1
        return node.value

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.head.value

    def size(self):
        return self._size

# Example:
if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue("a")
    q.enqueue("b")
    print(q.dequeue())  # "a"
    print(q.front())    # "b"
