class Solution:
    def merge(self, left, right):
        # Merges two sorted lists into one sorted list
        merged = []
        i = j = 0

        # Compare elements from both lists and merge them in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append remaining elements (only one of these loops will run)
        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def mergeSort(self, nums):
        # Base case: list of length 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums

        # Split the list into two halves
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        # Merge the sorted halves
        return self.merge(left, right)

    def sortArray(self, nums):
        # LeetCode requires returning the sorted array
        return self.mergeSort(nums)
