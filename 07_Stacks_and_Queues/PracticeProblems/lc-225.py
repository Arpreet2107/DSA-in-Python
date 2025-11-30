# ✅ LeetCode 225 — Implement Stack Using Queues
# 📌 Goal

# Implement a stack (LIFO) using only queue operations.

# Allowed queue operations:

# push(x)

# pop()

# peek()

# empty()

# All operations of a normal queue: enqueue, dequeue, size, empty.

# 🎯 Approach — Using ONE Queue Only (Efficient)

# We will simulate a stack behavior using just one queue:

# 👉 How does it work?

# When we push(x), we first enqueue it like normal.

# Then rotate the queue so that x comes to the front.

# This ensures:

# Most recently added element is always at front → stack top.

# pop() becomes O(1).

# top() becomes O(1).

# Time Complexity
# | Operation | Complexity      |
# | --------- | --------------- |
# | push      | O(n) (rotation) |
# | pop       | O(1)            |
# | top       | O(1)            |
# | empty     | O(1)            |
from collections import deque

class MyStack:

    def __init__(self):
        # Using one queue to simulate stack behavior
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element onto stack.
        Steps:
        1. Add x to the queue.
        2. Rotate the queue to bring x to the front.
        This ensures LIFO behavior.
        """
        self.q.append(x)  # normal enqueue

        # Rotate queue so that new element becomes the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack.
        Since top is always at the front of the queue,
        we simply dequeue.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element (front of the queue).
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns True if stack is empty.
        """
        return len(self.q) == 0

