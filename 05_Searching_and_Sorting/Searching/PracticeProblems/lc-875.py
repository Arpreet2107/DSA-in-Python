# # 🐒🍌 LeetCode 875 — Koko Eating Bananas
# # Problem Summary

# # Koko has piles of bananas and wants to eat them at a constant speed k bananas per hour.

# # Given:

# # piles: array of banana piles

# # h: number of hours Koko has

# # Goal:
# # 👉 Find the minimum integer k such that Koko can finish all bananas in h hours.

# # 🔥 Key Insight

# # If Koko eats faster, she finishes earlier.
# # If she eats slower, she finishes later.

# # This creates a monotonic function → perfect for binary search.
# 🎯 Observations
# Minimum possible eating speed:
# 1 banana/hour

# Maximum possible eating speed:
# max(piles)  # eat the largest pile in one hour


# So search space = [1 … max(piles)].

# 🧠 How to calculate hours required for a given speed k?

# For each pile:
# Koko needs:

# hours = ceil(pile / k)


# Without using math.ceil, we use integer math trick:

# (pile + k - 1) // k


# Total hours = sum over all piles.

# If total hours ≤ h → speed is enough → try smaller
# If total hours > h → too slow → increase speed

# 🔍 Binary Search Strategy

# left = 1

# right = max(piles)

# Always shrink search space until left == right → answer
class Solution:
    def minEatingSpeed(self, piles, h):
        
        # Function to compute total hours needed at eating speed 'k'
        def hoursNeeded(k):
            total = 0
            for pile in piles:
                # ceil(pile / k) = (pile + k - 1) // k
                total += (pile + k - 1) // k
            return total

        # Binary search boundaries
        left, right = 1, max(piles)

        # Binary search for minimum k
        while left < right:
            mid = (left + right) // 2

            # If mid speed allows finishing in 'h' hours or less → try smaller speed
            if hoursNeeded(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left  # or right
