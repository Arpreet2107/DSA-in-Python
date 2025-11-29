# ✅ LeetCode 237 — Delete Node in a Linked List
# 📘 Problem Summary

# You are not given the head of the linked list.
# You are only given a reference to the node that needs to be deleted.

# Example:

# Linked List: 4 → 5 → 1 → 9
# Delete node: 5


# But you don’t have the full list.
# You only have:

# node = reference to node with value 5

# ❗ Key Restriction

# You cannot reach the previous node, so you cannot do:

# prev.next = node.next


# because you don’t know who "prev" is.

# 💡 Smart Trick to Delete a Node

# Since you can’t delete the node itself, you:

# ✔ Copy the value of the next node into the current node
# ✔ Then delete the next node instead

# Example:

# Before:

# node → [5] → [1] → ...


# Copy next value inside:

# node.val = node.next.val   → becomes 1


# Skip the next node:

# node.next = node.next.next


# Now list becomes:

# 4 → 1 → 9


# The original 5 is gone!

# 🧠 Why This Works?

# Because in a singly linked list:

# You can modify current node

# But you cannot reach previous node

# So we simulate deletion by:

# Overwriting current node with the next node

# Skipping the next node (effectively deleting it)
class Solution:
    def deleteNode(self, node):
        """
        Deletes a node from a singly linked list
        when only the node itself is given.

        Strategy:
        1. Copy value from next node into current node.
        2. Skip over the next node.
        """

        # Step 1: Copy the value from the next node
        node.val = node.next.val

        # Step 2: Link current node to the node after next
        node.next = node.next.next
# ⏱ Complexity Analysis
# | Operation | Complexity |
# | --------- | ---------- |
# | Time      | **O(1)**   |
# | Space     | **O(1)**   |
