# circular_linked_list.py

class CNode:
    """
    Node for a circular singly linked list.
    Each node has data and next pointer. The last node points back to head.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    """
    Circular singly linked list where tail.next == head.
    We'll maintain a tail pointer (None if empty) for convenient operations.
    """
    def __init__(self):
        self.tail = None  # tail.next points to head; tail is None when list empty

    def is_empty(self):
        return self.tail is None

    def traverse(self):
        """
        Return list of values. Take care not to loop infinitely.
        O(n) time.
        """
        values = []
        if not self.tail:
            return values
        current = self.tail.next  # head = tail.next
        while True:
            values.append(current.data)
            current = current.next
            if current == self.tail.next:  # full circle
                break
        return values

    def insert_at_head(self, data):
        """
        Insert new node at head position (i.e., after tail).
        O(1) time.
        """
        new_node = CNode(data)
        if not self.tail:
            # empty list: new_node points to itself and is tail
            new_node.next = new_node
            self.tail = new_node
            return
        # insert new_node after tail, making it the new head
        new_node.next = self.tail.next
        self.tail.next = new_node

    def insert_at_tail(self, data):
        """
        Insert at tail (after current tail), then update tail pointer.
        O(1) time.
        """
        self.insert_at_head(data)  # insert new node as head
        self.tail = self.tail.next  # move tail to new node (which was head)

    def delete_head(self):
        """
        Delete head node. Handle single-node list separately.
        O(1) time.
        """
        if not self.tail:
            raise IndexError("Deleting from empty list")
        head = self.tail.next
        if head == self.tail:
            # only one node
            self.tail = None
        else:
            # bypass head
            self.tail.next = head.next

    def delete_by_value(self, target):
        """
        Delete first occurrence of target. Returns True if deleted else False.
        O(n) time.
        """
        if not self.tail:
            return False
        prev = self.tail
        cur = self.tail.next  # start at head
        while True:
            if cur.data == target:
                # found; remove cur
                if cur == prev:
                    # only one node
                    self.tail = None
                else:
                    prev.next = cur.next
                    if cur == self.tail:
                        # if deleting tail, update tail
                        self.tail = prev
                return True
            prev, cur = cur, cur.next
            if cur == self.tail.next:  # completed full circle
                break
        return False

    # convenience: build from iterable
    def from_list(self, iterable):
        self.tail = None
        for v in iterable:
            self.insert_at_tail(v)
if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
    cll.insert_at_tail(10)  # [10]
    cll.insert_at_tail(20)  # [10,20]
    cll.insert_at_tail(30)  # [10,20,30]
    print("Circular list:", cll.traverse())  # prints [10,20,30]
    cll.delete_by_value(20)
    print("After delete:", cll.traverse())
    cll.delete_head()
    print("After deleting head:", cll.traverse())
