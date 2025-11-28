# singly_linked_list.py

class Node:
    """
    Node for a singly linked list.
    Each node stores 'data' and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data      # the value stored in this node
        self.next = None      # reference to the next node (None by default)


class SinglyLinkedList:
    """
    Singly linked list supporting:
    - traverse (print)
    - insert at head
    - insert at tail
    - insert after a value (or at index)
    - delete by value
    - delete at index
    """
    def __init__(self):
        self.head = None      # head points to the first node (None if list empty)

    def traverse(self):
        """
        Traverse the list from head to end and return list of values.
        O(n) time, O(1) extra space.
        """
        values = []                   # collect node values for easy return/display
        current = self.head           # start at head
        while current:                # loop until current becomes None
            values.append(current.data)
            current = current.next    # move to next node
        return values

    def insert_at_head(self, data):
        """
        Insert new node at the beginning of the list.
        O(1) time.
        """
        new_node = Node(data)         # create the new node
        new_node.next = self.head     # link new node to current head
        self.head = new_node          # update head to new node

    def insert_at_tail(self, data):
        """
        Insert new node at the end of the list.
        O(n) time if no tail pointer; O(1) if we maintained tail reference.
        """
        new_node = Node(data)
        if not self.head:             # empty list case
            self.head = new_node      # new node becomes head
            return
        current = self.head
        while current.next:           # traverse to last node
            current = current.next
        current.next = new_node       # link last node to new node

    def insert_after_value(self, target, data):
        """
        Insert new node with 'data' after the first node that has value == target.
        If target not found, raises ValueError.
        O(n) time.
        """
        current = self.head
        while current and current.data != target:
            current = current.next
        if not current:
            raise ValueError(f"Value {target} not found in list.")
        new_node = Node(data)
        new_node.next = current.next  # link new node to next of target node
        current.next = new_node       # link target node to new node

    def delete_by_value(self, target):
        """
        Delete first node with value == target.
        Returns True if deleted, False if not found.
        O(n) time.
        """
        current = self.head
        prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        if not current:
            return False               # not found
        if not prev:
            # deleting head
            self.head = current.next
        else:
            # bypass current node
            prev.next = current.next
        return True

    def delete_at_index(self, index):
        """
        Delete node at given index (0-based).
        Raises IndexError if out of bounds.
        O(n) time.
        """
        if index < 0:
            raise IndexError("Index must be non-negative.")
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if not current:
            raise IndexError("Index out of bounds.")
        if not prev:
            # remove head
            self.head = current.next
        else:
            prev.next = current.next

    # Optional: helper to build list from Python iterable (for convenience)
    def from_list(self, iterable):
        """Create linked list from iterable (clears existing list)."""
        self.head = None
        for value in iterable:
            self.insert_at_tail(value)
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_head(10)          # [10]
    sll.insert_at_tail(20)          # [10,20]
    sll.insert_at_tail(30)          # [10,20,30]
    sll.insert_after_value(20, 25)  # [10,20,25,30]
    print("Traverse:", sll.traverse())  # prints [10,20,25,30]
    sll.delete_by_value(25)         # [10,20,30]
    sll.delete_at_index(0)          # remove head -> [20,30]
    print("After deletions:", sll.traverse())
