# ✅ LeetCode 160 — Intersection of Two Linked Lists

# Difficulty: Easy
# Topics: Linked List, Two Pointers

# 🧠 Problem Summary

# You are given two singly linked lists:
# They may or may not intersect.
# If they intersect, return the node where they meet.
# If not, return None.

# Example:

# List A: 4 → 1
#                  ↘
#                   8 → 4 → 5
#                  ↗
# List B:     5 → 0 → 1


# Intersection at node 8.

# 🧠 Key Intuition (The Famous Two-Pointer Trick)

# Use two pointers:

# ptrA starts at headA

# ptrB starts at headB

# Move both pointers forward at the same speed.

# When one pointer reaches the end, redirect it to the other list’s head.

# Why does this work?

# Because by switching heads:

# Both pointers travel equal total distance

# If intersection exists → they will meet at the intersection node

# If no intersection → both will become None at the same time

# Total distance traveled:
# ptrA travels: A + B
# ptrB travels: B + A


# Thus they equalize.

# 🎯 Time & Space Complexity
# | Complexity | Value    |
# | ---------- | -------- |
# | Time       | O(m + n) |
# | Space      | O(1)     |

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x           # node value
        self.next = None       # pointer to next node


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # If either list is empty → intersection impossible
        if not headA or not headB:
            return None
        
        # Two pointers start at the heads of both lists
        ptrA = headA
        ptrB = headB
        
        # Continue until both pointers meet (either at intersection or both None)
        while ptrA is not ptrB:
            
            # If ptrA reaches end, redirect to headB
            ptrA = ptrA.next if ptrA else headB
            
            # If ptrB reaches end, redirect to headA
            ptrB = ptrB.next if ptrB else headA
        
        # Either intersection node OR None if no intersection
        return ptrA
