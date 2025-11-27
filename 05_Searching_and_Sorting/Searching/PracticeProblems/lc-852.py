# ⛰️ LeetCode 852 — Peak Index in a Mountain Array
# Problem Summary

# You are given a mountain array → an array that:

# Strictly increases until a peak

# Then strictly decreases

# Example:
# [0, 2, 5, 7, 6, 4, 1]
# Peak index = 3 (value = 7)

# Your task: Return the index of the peak element.

# 🔥 Why Binary Search?

# Because the array shape guarantees:

# On the left of peak: arr[mid] < arr[mid + 1] (increasing slope)

# On the right of peak: arr[mid] > arr[mid + 1] (decreasing slope)

# This is perfect for binary search because we can remove half of the search space every step.

# 🧠 Binary Search Logic

# At each mid:

# ✔ Case 1: arr[mid] < arr[mid + 1]

# You are on the left side of the mountain
# → The peak is to the right
# → Move left = mid + 1

# ✔ Case 2: arr[mid] > arr[mid + 1]

# You are on the right side of the mountain
# → The peak is at mid or to the left
# → Move right = mid

# Eventually, left == right → pointing to the peak.
class Solution:
    def peakIndexInMountainArray(self, arr):
        # Two pointers for binary search
        left, right = 0, len(arr) - 1

        # Binary search for the peak
        while left < right:
            mid = (left + right) // 2

            # If mid is smaller than its next element → we are on increasing slope
            if arr[mid] < arr[mid + 1]:
                # Peak is toward the right
                left = mid + 1
            else:
                # We are on decreasing slope → peak is at mid or left of mid
                right = mid

        # When left == right, both are pointing to the peak index
        return left
