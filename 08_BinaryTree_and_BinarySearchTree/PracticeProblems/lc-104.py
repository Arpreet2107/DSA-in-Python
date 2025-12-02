# 🌳 LeetCode 104 — Maximum Depth of Binary Tree
# 📘 Problem Summary

# Given the root of a binary tree, return the maximum depth.
# Depth = number of nodes along the longest path from root → leaf.

# Example:

#       3
#      / \
#     9  20
#        / \
#       15  7

# Max Depth = 3

# ✅ Approach 1: DFS (Recursive) — Most Common
# Logic

# Height of a tree =
# 1 + max(height of left subtree, height of right subtree)

# If node is None, height = 0.
# Definition for a binary tree node.
# 🧠 Time & Space Complexity
# | Method | Time     | Space                |
# | ------ | -------- | -------------------- |
# | DFS    | **O(N)** | O(H) recursive stack |
# | BFS    | **O(N)** | O(W) queue width     |

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # store node value
        self.left = left    # left child
        self.right = right  # right child


class Solution:
    def maxDepth(self, root):
        # If the tree is empty, depth is 0
        if not root:
            return 0

        # Recursive function to compute depth
        def dfs(node):
            # Base case: if node is None, return 0
            if not node:
                return 0

            # Recursively compute left subtree depth
            left_depth = dfs(node.left)

            # Recursively compute right subtree depth
            right_depth = dfs(node.right)

            # Current node depth = 1 + maximum of child depths
            return 1 + max(left_depth, right_depth)

        # Call dfs starting from root
        return dfs(root)
# ✅ Approach 2: BFS (Level Order Traversal)

# Also valid. Count how many levels exist.
from collections import deque

class Solution:
    def maxDepth(self, root):
        # If tree is empty
        if not root:
            return 0

        queue = deque([root])  # queue to perform level-order traversal
        depth = 0              # track levels

        # While there are nodes to process
        while queue:
            level_size = len(queue)  # number of nodes in current level
            depth += 1               # increase depth for each level

            # Process all nodes in this level
            for _ in range(level_size):
                node = queue.popleft()    # remove from queue

                # Push left child if exists
                if node.left:
                    queue.append(node.left)

                # Push right child if exists
                if node.right:
                    queue.append(node.right)

        # Depth after processing all levels
        return depth
