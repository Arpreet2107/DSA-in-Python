# ✅ LeetCode 232 — Implement Queue using Two Stacks

# We must implement a FIFO queue using two LIFO stacks.

# 🔥 Core Logic

# We use two stacks:

# 👉 stack_in

# Used for enqueue (push) operations.

# 👉 stack_out

# Used for dequeue (pop) and peek.

# Why two stacks?

# When we need to pop() or peek(), if stack_out is empty,
# we transfer all elements from stack_in → stack_out
# (this reverses the order → making it FIFO).

# Time Complexity:

# Amortized O(1) for push/pop/peek
class MyQueue:

    def __init__(self):
        # stack_in is used for enqueue (push) operations
        self.stack_in = []
        
        # stack_out is used for dequeue (pop) and peek operations
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Enqueue operation: simply push to stack_in.
        This is always O(1).
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Dequeue operation:
        If stack_out is empty, we move all elements from stack_in to stack_out.
        This reverses the order, allowing FIFO behavior.
        """
        # If stack_out has no elements, fill it by reversing stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # Now the oldest element is on top of stack_out
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Return the element at the front of the queue without removing it.
        Same logic as pop(), but we only return stack_out[-1].
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Queue is empty only when both stacks have no elements.
        """
        return not self.stack_in and not self.stack_out
# 📝 Explanation
# | Operation | Logic                                         | Time           |
# | --------- | --------------------------------------------- | -------------- |
# | `push(x)` | Put in `stack_in`                             | O(1)           |
# | `pop()`   | If needed → transfer to `stack_out`, then pop | Amortized O(1) |
# | `peek()`  | Same transfer logic, then return top          | Amortized O(1) |
# | `empty()` | Check both stacks                             | O(1)           |

