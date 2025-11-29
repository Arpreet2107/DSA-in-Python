# ✅ LeetCode 2 — Add Two Numbers

# Difficulty: Medium
# Topics: Linked List, Math, Simulation

# 🧠 Problem Summary

# You're given two linked lists:

# Digits are stored in reverse order

# Each node contains a single digit (0–9)

# Add the two numbers and return the sum as a linked list in the same reverse order.

# Example

# Input:

# l1 = 2 → 4 → 3   (represents 342)
# l2 = 5 → 6 → 4   (represents 465)


# Output:

# 7 → 0 → 8        (represents 807)


# Because 342 + 465 = 807

# 🧠 Core Idea

# Simulate addition just like elementary school:

# Add digit-by-digit

# Keep a carry if sum is ≥ 10

# Create a new node for each digit in the result

# Continue until both lists and carry are processed

# 🔍 Why Linked List Makes This Interesting?

# The number is stored backwards, so:

# Least significant digit comes first

# This makes addition start from the head — convenient!

# Example:
# 2 → 4 → 3 = 342 (reverse order)

# 🔥 Steps to Solve

# Create a dummy node to build the result

# Use pointers to traverse both lists

# Extract values (use 0 when the list ends)

# Compute:

# total = val1 + val2 + carry
# digit = total % 10
# carry = total // 10


# Create a new node with the digit

# Move pointers forward

# After traversal, if carry > 0, add one more node
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val         # value of this node
        self.next = next       # pointer to the next node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Dummy head to easily build the resulting linked list
        dummy = ListNode()
        current = dummy        # pointer to build the new list
        
        carry = 0              # carry generated from sum of digits

        # Traverse until both lists are fully consumed AND no carry remains
        while l1 or l2 or carry:

            # If l1 still exists, take its value; else use 0
            val1 = l1.val if l1 else 0
            
            # If l2 still exists, take its value; else use 0
            val2 = l2.val if l2 else 0
            
            # Total sum of this position
            total = val1 + val2 + carry
            
            # Digit to store (only last digit)
            digit = total % 10
            
            # New carry for next iteration
            carry = total // 10
            
            # Create new node with the sum digit
            current.next = ListNode(digit)
            
            # Move to next newly created node
            current = current.next
            
            # Move forward in both lists if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the list that starts from dummy.next
        return dummy.next
