# file: queue_array.py

class CircularQueue:
    """
    Fixed-capacity circular queue using a list as buffer.
    Maintains head index (front) and tail index (next write position) and size.
    """

    def __init__(self, capacity=100):
        self._capacity = capacity
        self._data = [None] * capacity  # underlying buffer
        self._head = 0                   # index of current front element
        self._size = 0                   # number of elements present

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, value):
        # Add value to the tail position
        if self.is_full():
            raise IndexError("Enqueue to full queue")
        tail_index = (self._head + self._size) % self._capacity
        self._data[tail_index] = value
        self._size += 1

    def dequeue(self):
        # Remove and return value from head
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self._data[self._head]
        self._data[self._head] = None   # optional: clear reference
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._data[self._head]

    def size(self):
        return self._size

# Example:
if __name__ == "__main__":
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # 1
    q.enqueue(3)
    q.enqueue(4)
    # Now full
    print(q.front())    # 2
