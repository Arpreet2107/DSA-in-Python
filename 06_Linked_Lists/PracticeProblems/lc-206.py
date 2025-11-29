# ✅ LeetCode 206 — Reverse Linked List

# Difficulty: Easy
# Type: Linked List, Iterative / Recursive

# 🧠 Concept Explanation

# We need to reverse the direction of pointers in a singly linked list.

# Example:

# 1 → 2 → 3 → 4 → 5 → None

# After reversing:

# 5 → 4 → 3 → 2 → 1 → None

# We only need to change .next links — no new nodes are created.

# 🔄 Two Approaches
# ✔ Iterative (Most common)

# Uses 3 pointers:

# prev → the node behind

# current → the node being processed

# next_node → store next before changing links

# ✔ Recursive

# Elegant but requires call stack.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # value stored in the node
        self.next = next      # pointer to the next node


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverses a singly linked list using the iterative approach.
        """
        
        prev = None            # 'prev' will become the new head at the end
        current = head         # start with the original head
        
        # Traverse through the linked list
        while current:
            
            # Save the next node BEFORE breaking the link
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move prev and current one step forward
            prev = current
            current = next_node
        
        # 'prev' now points to the new head of the reversed list
        return prev
