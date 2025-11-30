# file: stack_linkedlist.py

class Node:
    # Node used by linked-list implementations
    def __init__(self, value, next_node=None):
        self.value = value      # stored value
        self.next = next_node   # pointer to next node


class LinkedListStack:
    """
    Stack implemented using a singly linked list.
    Push/pop happen at the head (top) in O(1) time.
    """

    def __init__(self):
        self.head = None   # head references top node; None if empty
        self._size = 0     # maintain size for O(1) size()

    def is_empty(self):
        return self.head is None

    def push(self, value):
        # Create new node and make it the new head
        node = Node(value, self.head)
        self.head = node
        self._size += 1

    def pop(self):
        # Remove head and return its value
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        node = self.head
        self.head = node.next
        node.next = None  # optional: help GC
        self._size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.value

    def size(self):
        return self._size

    def clear(self):
        # Walk and drop references; O(n), but sets head to None quickly
        self.head = None
        self._size = 0

# Example usage
if __name__ == "__main__":
    st = LinkedListStack()
    st.push("a")
    st.push("b")
    print(st.peek())   # b
    print(st.pop())    # b
    print(st.size())   # 1
