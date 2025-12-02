# ✅ LeetCode 98 — Validate Binary Search Tree

# A valid BST must follow strict rules:

# Left subtree values  <  root value  <  right subtree values


# This must hold for every node, not just immediate children.

# Example of a valid BST:

#       5
#      / \
#     3   7


# Example of an invalid BST:

#       5
#      / \
#     1   4
#        / \
#       3   6     ❌ 3 is on the right of 5 → invalid!


# To validate properly, we must ensure EVERY node lies within a valid numeric range.

# 🌟 Approach: DFS with Valid Ranges

# For each node:

# Node value must be strictly greater than a lower bound.

# Node value must be strictly smaller than an upper bound.

# Initially:

# (-∞, +∞)


# When going left:

# upper bound becomes node.val


# When going right:

# lower bound becomes node.val


# If any node violates its range → NOT a BST.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        
        def validate(node, low, high):
            # Empty subtree is valid
            if not node:
                return True
            
            # Current node must satisfy: low < node.val < high
            if not (low < node.val < high):
                return False
            
            # Validate left subtree (upper bound becomes node.val)
            left_is_valid = validate(node.left, low, node.val)
            
            # Validate right subtree (lower bound becomes node.val)
            right_is_valid = validate(node.right, node.val, high)
            
            return left_is_valid and right_is_valid
        
        # Call with full range
        return validate(root, float("-inf"), float("inf"))
