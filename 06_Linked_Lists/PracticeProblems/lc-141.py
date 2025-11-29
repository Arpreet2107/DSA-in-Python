# ✅ LeetCode 141 — Linked List Cycle
# Goal:

# Return True if the linked list has a cycle.
# Return False otherwise.

# A cycle means some node’s next pointer points back to a previous node instead of ending at None.

# 🧠 Intuition — Floyd’s Cycle Detection Algorithm

# We use two pointers:

# slow pointer (tortoise) → moves 1 step

# fast pointer (hare) → moves 2 steps

# Why does this detect a cycle?

# If the list has a cycle:

# Fast pointer moves twice as fast.

# Eventually, fast will “lap” slow and they will meet.

# If the list has no cycle:

# Fast will reach None and the algorithm stops.

# This is the most optimal solution.

# ⏱ Time & Space Complexity
# | Complexity | Value |                                 |
# | ---------- | ----- | ------------------------------- |
# | Time       | O(n)  |                                 |
# | Space      | O(1)  | ← constant space, best possible |

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x           # value stored in node
        self.next = None       # pointer to the next node


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # If there are 0 or 1 nodes, a cycle is impossible
        if not head or not head.next:
            return False

        # Initialize slow and fast pointers
        slow = head            # moves 1 step per iteration
        fast = head            # moves 2 steps per iteration

        # Loop until fast reaches end OR slow and fast meet
        while fast and fast.next:

            slow = slow.next          # slow moves 1 step
            fast = fast.next.next     # fast moves 2 steps

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # Fast reached null → no cycle
        return False
