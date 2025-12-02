# 🌪️ LeetCode 103 — Zigzag Level Order Traversal of a Binary Tree
# ✅ Problem Summary

# You're given the root of a binary tree.
# You must return its level-order traversal, but with a twist:

# Level 0 → left to right

# Level 1 → right to left

# Level 2 → left to right

# Level 3 → right to left

# … and so on

# This alternating pattern is the zigzag (or spiral) traversal.

# 🧠 Approach (BFS + Reverse Every Alternate Level)

# We perform normal BFS using a queue:

# Push root into queue.

# For each level, gather all nodes inside level_nodes.

# If it's an odd level → reverse level_nodes.

# Append to result.

# Continue BFS.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        # If the tree is empty, return empty list
        if not root:
            return []

        from collections import deque
        
        # Queue for BFS traversal
        queue = deque([root])

        # This will store the final zigzag order
        result = []

        # To know whether to reverse the level or not
        level = 0

        # BFS loop
        while queue:
            level_size = len(queue)  # Number of nodes in current level
            current_level = []       # To store nodes of this level

            # Process each node in the current level
            for _ in range(level_size):
                node = queue.popleft()  # Pop from queue

                current_level.append(node.val)

                # Add children to queue if present
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # If level is odd → reverse the current level values
            if level % 2 == 1:
                current_level.reverse()

            # Add to result
            result.append(current_level)

            # Move to next level
            level += 1

        return result
