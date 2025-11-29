# ✅ LeetCode 19. Remove Nth Node From End of List

# Difficulty: Medium
# Approach: Two–pointer (Fast & Slow Pointer)
# ✅ 🧠 Explanation (Simple Words)
# ✔ Step 1:

# Make a dummy node before head so deleting the first node is easy.

# ✔ Step 2:

# Move fast pointer n+1 steps ahead.

# ✔ Step 3:

# Move fast and slow together until fast becomes None.
# Now slow is at (node before the target node).

# ✔ Step 4:

# Delete the nth node by skipping it.

# ✔ Step 5:

# Return dummy.next as new head.

# 🧪 Example

# Input list: 1 -> 2 -> 3 -> 4 -> 5, n = 2
# Output: 1 -> 2 -> 3 -> 5
# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # store the value of the node
        self.next = next    # pointer to the next node


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        We will remove the nth node from the END of a linked list.
        The fastest way is to use TWO POINTERS:
        - fast pointer: moves n+1 steps ahead
        - slow pointer: starts from a dummy node
        ❗ When fast reaches the end, slow.next is the node to remove.
        """

        # Create a dummy node pointing to the head.
        # This helps handle cases like removing the first node.
        dummy = ListNode(0, head)

        # Initialize both fast and slow pointers at dummy.
        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        # so that the gap between fast and slow becomes n
        for _ in range(n + 1):
            fast = fast.next

        # Move fast to the end of the list
        # slow will then point to the node just before the node we want to delete
        while fast:
            fast = fast.next
            slow = slow.next

        # Now slow.next is the node to delete.
        # Remove it by skipping that node.
        slow.next = slow.next.next

        # Return the new head (dummy.next)
        return dummy.next
