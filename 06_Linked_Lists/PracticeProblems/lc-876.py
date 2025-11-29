# # ✅ LeetCode 876: Middle of the Linked List

# # Problem:
# # Given the head of a singly linked list, return the middle node.

# # If the list has odd number of nodes → return the exact middle

# # If the list has even number of nodes → return the second middle node

# # ✅ Intuition (Slow + Fast Pointer Technique)

# # We use two pointers:

# # slow → moves 1 step at a time

# # fast → moves 2 steps at a time

# # 👉 When fast reaches the end of the list,
# # 👉 slow will be at the middle of the list.

# # This works because fast moves at double the speed.

# # Example:
# # 1 → 2 → 3 → 4 → 5 → null

# # slow path = 1,2,3

# # fast path = 1,3,5
# # Middle = 3

# # If even number of nodes:
# # 1 → 2 → 3 → 4 → null

# # slow path = 1,2,3

# # fast path = 1,3,null
# # Middle = 3 (the second middle)

# # 🧠 Time & Space Complexity
# | Operation | Complexity             |
# | --------- | ---------------------- |
# | Time      | **O(n)** (single pass) |
# | Space     | **O(1)**               |
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Find the middle of a singly linked list using
        the slow and fast pointer technique.
        """

        slow = head  # slow pointer moves 1 step
        fast = head  # fast pointer moves 2 steps

        # Loop until fast reaches the end of the list
        while fast and fast.next:
            slow = slow.next          # move slow pointer 1 step
            fast = fast.next.next     # move fast pointer 2 steps

        # slow will now be at the middle node
        return slow
