# ✅ LIS using Patience Sorting – O(n log n)
# Best optimized method, used in competitive programming.
import bisect

def lengthOfLIS_fast(nums):
    """
    LIS using Patience Sorting (Binary Search)
    Time: O(n log n)
    
    tails[k] = smallest ending number of an LIS of length k+1
    """

    tails = []

    for num in nums:
        # Find position in tails using binary search
        pos = bisect.bisect_left(tails, num)

        # If pos == len(tails), extend the list
        if pos == len(tails):
            tails.append(num)
        else:
            # Replace the value to maintain smallest possible tail
            tails[pos] = num

    return len(tails)
