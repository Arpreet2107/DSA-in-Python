# 🔽 LeetCode 107 — Binary Tree Level Order Traversal II
# ✅ Problem Summary

# You are given the root of a binary tree.
# You must return the level order traversal, but from bottom to top.

# Example:

# Tree:
#       3
#      / \
#     9   20
#         / \
#        15  7


# Normal Level Order (Top → Bottom):

# [[3], [9, 20], [15, 7]]


# Required Output (Bottom → Top):

# [[15, 7], [9, 20], [3]]

# 🧠 Approach: BFS + Reverse at the End

# We simply perform a regular BFS and collect levels:

# Use a queue

# Process each level

# Append the list of values

# After BFS completes → reverse the result

# Time Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        # If the root is None, return an empty list
        if not root:
            return []

        from collections import deque

        queue = deque([root])  # BFS queue
        result = []            # Stores normal top-down level order

        # Standard BFS traversal
        while queue:
            level_size = len(queue)   # Number of nodes at this level
            current_level = []        # List for nodes in this level

            # Process all nodes at this level
            for _ in range(level_size):
                node = queue.popleft()

                current_level.append(node.val)

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append this level's values
            result.append(current_level)

        # For bottom-up order, simply reverse the list
        return result[::-1]
