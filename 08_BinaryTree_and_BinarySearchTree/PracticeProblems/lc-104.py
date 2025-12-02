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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        # Base case: Empty tree has depth 0
        if not root:
            return 0
        
        # Recursively find the depth of left subtree
        left_depth = self.maxDepth(root.left)
        
        # Recursively find the depth of right subtree
        right_depth = self.maxDepth(root.right)
        
        # Current node contributes +1 to the height
        return 1 + max(left_depth, right_depth)

# ✅ Approach 2: BFS (Level Order Traversal)

# Also valid. Count how many levels exist.
from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        # Level order traversal
        while queue:
            depth += 1
            level_size = len(queue)
            
            # Traverse all nodes in this level
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
