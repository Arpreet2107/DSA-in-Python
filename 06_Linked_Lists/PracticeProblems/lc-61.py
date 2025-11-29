# ✅ LeetCode 61 — Rotate List

# Difficulty: Medium
# Topic: Linked List, Two Pointers, Circular List

# 🧠 Understanding the Problem

# You are given a linked list and a number k.
# You must rotate the list to the right by k places.

# Example

# Input:
# 1 → 2 → 3 → 4 → 5, k = 2

# Output:
# 4 → 5 → 1 → 2 → 3

# Why?

# Rotate right by 1:
# 5 → 1 → 2 → 3 → 4
# Rotate right by 2:
# 4 → 5 → 1 → 2 → 3

# 🔍 Key Observations
# ✔ 1. Rotating by list size does nothing

# If list length = 5
# Rotate by k = 5 → same list
# So we use: k = k % length

# ✔ 2. Convert list to a circle

# If we link the tail to the head:
# 1 → 2 → 3 → 4 → 5 ↺

# Now rotating is just choosing a new break point.

# ✔ 3. New tail position

# The new tail is at index:
# length - k - 1

# The new head is:
# new_tail.next

# Then break the circle.
# Definition for singly linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # node value
        self.next = next      # pointer to next node


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # If list is empty or one node or k = 0 → no change needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the linked list
        length = 1
        tail = head
        
        # Move to the last node to count length
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Make the list circular
        tail.next = head
        
        # Step 3: Normalize k (because rotating length times gives original list)
        k = k % length
        
        # Number of steps to reach the new tail:
        # It will be the (length - k - 1)th node from the start
        steps_to_new_tail = length - k - 1
        
        new_tail = head
        # Move forward steps_to_new_tail times
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # New head is next of new_tail
        new_head = new_tail.next
        
        # Step 4: Break the circle
        new_tail.next = None
        
        # Return new rotated head
        return new_head
