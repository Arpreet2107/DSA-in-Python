# # 🟦 LeetCode 300 — Longest Increasing Subsequence (LIS)
# # Approach: Patience Sorting + Binary Search (O(n log n))

# # We maintain an array tails where:

# # tails[k] = the smallest possible tail of an increasing subsequence of length k+1.

# # For each number, we use binary search to find where it should go.

# # This guarantees O(n log n) performance.
# 🧠 Concept Summary
# ✔ Why does “tails” work?

# tails[k] = smallest ending number of an increasing subsequence of length k+1.

# Smaller tails allow more room for future numbers to build longer sequences.

# ✔ Why binary search?

# To find the first position where num is not smaller → correct place to update LIS tail.
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        We use the Patience Sorting technique.
        'tails' stores the minimum tail value for all LIS of each length.
        Binary search decides where to place each number.
        """

        from bisect import bisect_left

        # 'tails' will store the smallest ending values
        # of increasing subsequences of different lengths.
        tails = []

        # Iterate through every number in the input array
        for num in nums:

            # Find the index where 'num' should be placed
            # bisect_left returns first index where num <= tails[idx]
            index = bisect_left(tails, num)

            # Case 1: num is larger than all tails → extend LIS
            if index == len(tails):
                tails.append(num)

            # Case 2: Replace an existing tail with a smaller value
            # This helps reduce future tail values → more LIS opportunities
            else:
                tails[index] = num

        # Length of tails array = length of LIS
        return len(tails)
