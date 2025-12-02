# ✅ LeetCode 215 — Kth Largest Element in an Array

# Given an unsorted array, return the k-th largest element.

# Example:

# nums = [3,2,1,5,6,4], k = 2
# → Answer = 5  (2nd largest)

# ⭐ Best Approaches
# Approach 1: Sort the Array (Simple)

# Sort descending

# Return nums[k-1]

# Time: O(N log N)
# Space: O(1)

# But not the most optimal.

# ⭐ Approach 2 (Recommended): Min-Heap of size k

# Maintain a min-heap that keeps k largest elements only

# If heap size > k → pop smallest

# Top of heap = k-th largest

# Time: O(N log k)
# Space: O(k)

# Very efficient.

# ⭐ Approach 3: Quickselect (Optimal on Average)

# Quickselect = the selection version of Quicksort
# Average time O(N), worst-case O(N²)
# Used in many interviews.
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Create a min-heap
        min_heap = []

        for num in nums:
            # Push current number
            heapq.heappush(min_heap, num)

            # Keep heap size exactly k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Root of heap is the kth largest
        return min_heap[0]
