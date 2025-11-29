# ✅ LeetCode 83 — Remove Duplicates From Sorted List

# Difficulty: Easy
# Key Point: List is sorted, so duplicates will always appear next to each other.

# 🧠 Approach (Simple Explanation)

# We simply walk through the list, and whenever two consecutive nodes have the same value, we skip the duplicate by adjusting the next pointer.

# ✔ Only one pointer (current) is needed
# ✔ O(n) time — we visit each node once
# ✔ O(1) space — no extra memory
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # store value of node
        self.next = next      # pointer to next node


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Removes ALL duplicates from a sorted linked list.
        Since the list is sorted, duplicates always appear consecutively.
        """

        # If list is empty or has only 1 node → no duplicates possible
        if not head:
            return head

        # Start from the first node
        current = head

        # Traverse the entire linked list
        while current and current.next:

            # If next node has same value → skip it
            if current.val == current.next.val:
                # bypass the duplicate node
                current.next = current.next.next
            else:
                # move forward only when values differ
                current = current.next

        # return the updated list head
        return head
