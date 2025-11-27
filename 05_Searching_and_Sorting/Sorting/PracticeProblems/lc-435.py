# ✅ LeetCode 435 — Non-Overlapping Intervals
# Problem Summary

# You are given a list of intervals where each interval is [start, end].

# Your goal:

# 👉 Remove the minimum number of intervals so that the rest do NOT overlap.

# Return how many intervals you must remove.

# 🎯 Key Idea (Greedy Algorithm)

# This is a classic greedy interval scheduling problem.

# We solve it using this strategy:

# 1️⃣ Sort intervals by their END time

# Why?
# Because choosing intervals that end earlier leaves more room for future intervals.

# This is the exact same logic used in "Activity Selection".

# 🔥 Main Logic

# After sorting by end time:

# Keep track of the end time of the last non-overlapping interval

# For each new interval:

# If its start time is >= last_end, it does NOT overlap → keep it

# Otherwise → it overlaps, so we must remove it

# We count how many overlapping intervals are removed.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        # If no intervals, nothing to remove
        if not intervals:
            return 0
        
        # Step 1: Sort intervals by the END time (interval[1])
        intervals.sort(key=lambda x: x[1])
        
        # We will keep count of non-overlapping intervals
        count = 1   # the first interval (after sorting) will always be included
        
        # Track the end time of the last included interval
        last_end = intervals[0][1]
        
        # Step 2: Iterate through the remaining intervals
        for start, end in intervals[1:]:
            
            # Case 1: If current interval does NOT overlap
            if start >= last_end:
                count += 1          # We keep this interval
                last_end = end      # Update the end boundary
            
            # Case 2: If it overlaps → we skip it (i.e., remove it)
            # No action needed because "removal" means not counting it
        
        # Total intervals - number of intervals we kept = removed intervals
        return len(intervals) - count
