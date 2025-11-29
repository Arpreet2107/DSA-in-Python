# ✅ LeetCode 142 — Linked List Cycle II
# Problem Summary

# You are given the head of a linked list.

# If the linked list contains a cycle, return the node where the cycle begins.

# If no cycle exists, return None.

# ❗ You are NOT allowed to modify the linked list.
# 🎯 Approach — Floyd’s Tortoise and Hare Algorithm

# This is the extended version of the cycle detection algorithm (used in LC 141), but with an additional step to find where the cycle begins.

# STEP 1 → Detect if a cycle exists

# Use two pointers:

# slow moves 1 step at a time

# fast moves 2 steps at a time

# If they meet → a cycle exists.

# If fast reaches None → no cycle.

# STEP 2 → Find Entry Point of the Cycle

# Once pointers meet:

# Reset one pointer (slow) to the head.

# Move both pointers 1 step at a time.

# The node at which they meet again → cycle entry point.

# 🧠 Why does this work?

# Because the distance from head to cycle start == distance from meeting point to cycle start.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # If list is empty or has a single node → cannot have a cycle
        if not head or not head.next:
            return None

        # Step 1: Use two pointers slow and fast to detect a cycle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # slow moves 1 step
            fast = fast.next.next     # fast moves 2 steps

            # If slow and fast meet → a cycle exists
            if slow == fast:
                break

        else:
            # If the while loop ends normally (no break)
            # That means no cycle exists
            return None

        # Step 2: Find the entry point of the cycle
        # Reset slow back to the head
        slow = head

        # Now move both slow and fast 1 step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # When they meet → that's where the cycle begins
        return slow
