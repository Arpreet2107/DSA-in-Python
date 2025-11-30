# file: deque_linked.py

class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedDeque:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # back
        self._size = 0

    def is_empty(self):
        return self.head is None

    def append(self, value):   # add to back
        node = DNode(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def appendleft(self, value):  # add to front
        node = DNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty deque")
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return node.value

    def popleft(self):
        if self.is_empty():
            raise IndexError("Popleft from empty deque")
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return node.value
