# file: stack_array.py

class ArrayStack:
    """
    Fixed-capacity stack implemented using a Python list as the backing array.
    This mimics a typical array-based stack with explicit capacity and top index.
    """

    def __init__(self, capacity=100):
        # Initialize the backing array with None placeholders for fixed capacity
        self._capacity = capacity            # maximum number of elements allowed
        self._data = [None] * self._capacity # fixed-size list (array)
        self._top = -1                       # index of top element; -1 means empty

    def is_empty(self):
        # Stack is empty when top == -1
        return self._top == -1

    def is_full(self):
        # Stack is full when top == capacity - 1
        return self._top == self._capacity - 1

    def push(self, value):
        # Add value on top — raise error if full
        if self.is_full():
            raise IndexError("Push to full stack")
        # advance top and place value
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        # Remove and return top element — raise error if empty
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self._data[self._top]  # read top value
        self._data[self._top] = None   # optional: clear reference
        self._top -= 1                 # move top down
        return value

    def peek(self):
        # Return top element without removing
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._data[self._top]

    def size(self):
        # Number of elements is top + 1
        return self._top + 1

    def clear(self):
        # Reset stack to empty; optionally clear array slots
        self._data = [None] * self._capacity
        self._top = -1

# Example usage (manual test)
if __name__ == "__main__":
    s = ArrayStack(5)
    s.push(10)
    s.push(20)
    print("top:", s.peek())   # 20
    print("pop:", s.pop())    # 20
    print("size:", s.size())  # 1
