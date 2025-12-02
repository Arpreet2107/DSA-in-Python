def is_balanced(root):
    # Return (is_balanced_bool, height) in one traversal
    def helper(node):
        if not node:
            return True, 0
        left_bal, left_h = helper(node.left)
        if not left_bal: return False, 0
        right_bal, right_h = helper(node.right)
        if not right_bal: return False, 0
        return abs(left_h - right_h) <= 1, 1 + max(left_h, right_h)
    balanced, _ = helper(root)
    return balanced
