# doubly_linked_list.py

class DNode:
    """
    Node for a doubly linked list.
    Stores 'data', reference to previous node, and reference to next node.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None  # previous node reference
        self.next = None  # next node reference


class DoublyLinkedList:
    """
    Doubly linked list supports:
    - traverse forward/backward
    - insert at head/tail
    - insert after a value
    - delete by value
    Having prev pointers makes some operations easier (O(1) deletions given node).
    """
    def __init__(self):
        self.head = None
        self.tail = None  # keep a tail pointer for O(1) tail operations

    def traverse_forward(self):
        """Return list of values from head to tail."""
        values = []
        cur = self.head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return values

    def traverse_backward(self):
        """Return list of values from tail to head."""
        values = []
        cur = self.tail
        while cur:
            values.append(cur.data)
            cur = cur.prev
        return values

    def insert_at_head(self, data):
        new_node = DNode(data)
        if not self.head:
            # empty list — head and tail both point to new node
            self.head = self.tail = new_node
            return
        # link new_node before current head
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = DNode(data)
        if not self.tail:
            # empty list
            self.head = self.tail = new_node
            return
        # append after tail
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after_value(self, target, data):
        """
        Insert after the first node with value == target.
        """
        cur = self.head
        while cur and cur.data != target:
            cur = cur.next
        if not cur:
            raise ValueError(f"Value {target} not found.")
        new_node = DNode(data)
        nxt = cur.next
        # Insert new_node between cur and nxt
        cur.next = new_node
        new_node.prev = cur
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node
        else:
            # inserted at the end -> update tail
            self.tail = new_node

    def delete_by_value(self, target):
        """
        Delete first node with value == target.
        Returns True if deleted, False if not found.
        """
        cur = self.head
        while cur and cur.data != target:
            cur = cur.next
        if not cur:
            return False
        # If cur is head
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        # If cur is tail
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev
        return True

    # convenience: build from iterable
    def from_list(self, iterable):
        self.head = self.tail = None
        for v in iterable:
            self.insert_at_tail(v)
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_head(10)    # [10]
    dll.insert_at_tail(20)    # [10,20]
    dll.insert_at_tail(30)    # [10,20,30]
    dll.insert_after_value(20, 25)  # [10,20,25,30]
    print("Forward:", dll.traverse_forward())   # [10,20,25,30]
    print("Backward:", dll.traverse_backward()) # [30,25,20,10]
    dll.delete_by_value(25)
    print("After delete:", dll.traverse_forward())
