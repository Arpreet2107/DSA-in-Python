# ✅ LeetCode 199 — Binary Tree Right Side View
# Problem Summary

# You are given the root of a binary tree.
# You must return the values of the nodes that are visible from the right side.

# That means:
# → For every level, return the rightmost node.

# ✅ Approach 1: BFS (Level Order Traversal)

# This is the easiest and most intuitive method.

# Logic

# Use a queue for level-by-level traversal.

# For each level:

# Traverse all nodes.

# The last node in that level is the one visible from the right side.

# Append that value into the answer list.
# Definition for a binary tree node.
# 🧠 Time & Space Complexity:
# | Method         | Time     | Space    |
# | -------------- | -------- | -------- |
# | BFS Right Side | **O(N)** | **O(N)** |

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Each node stores a value
        self.val = val
        # Pointer to left child
        self.left = left
        # Pointer to right child
        self.right = right


class Solution:
    def rightSideView(self, root):
        # If tree is empty, return empty list
        if not root:
            return []

        # This list will store the final right side view
        result = []

        # Use a queue to perform level-order traversal (BFS)
        from collections import deque
        queue = deque([root])  # Start with the root node

        # Loop until the queue is empty
        while queue:
            # Number of nodes in the current level
            level_size = len(queue)

            # Iterate over each node in this level
            for i in range(level_size):
                node = queue.popleft()  # Pop node from the front

                # If this is the *last node* in this level,
                # it is visible from the right side
                if i == level_size - 1:
                    result.append(node.val)

                # Push left child into queue if it exists
                if node.left:
                    queue.append(node.left)

                # Push right child into queue if it exists
                if node.right:
                    queue.append(node.right)

        # Return the list of right side view values
        return result
