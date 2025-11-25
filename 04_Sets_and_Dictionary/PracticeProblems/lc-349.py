from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert nums1 to a set to remove duplicates
        set1 = set(nums1)

        # Convert nums2 to a set to remove duplicates
        set2 = set(nums2)

        # Intersection of both sets gives common unique elements
        result = set1.intersection(set2)

        # Convert the set back to a list for the final output
        return list(result)


# ------------------------ MAIN FUNCTION ------------------------

if __name__ == "__main__":
    # Sample input arrays
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    # Create Solution object
    obj = Solution()

    # Call the intersection method
    output = obj.intersection(nums1, nums2)

    # Print final output
    print("Intersection of the two arrays is:", output)
