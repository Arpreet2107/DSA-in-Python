class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            mn = nums[i]        # assume current element is minimum
            ind = i             # store index of minimum

            # find position of real minimum in remaining array
            for j in range(i+1, n):
                if nums[j] < mn:
                    mn = nums[j]
                    ind = j

            # swap AFTER inner loop ends
            nums[i], nums[ind] = nums[ind], nums[i]

        return nums
