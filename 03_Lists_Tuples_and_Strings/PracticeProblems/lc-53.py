class Solution:
    def maxSubArray(self,nums:list[int])-> int:
        curr_sum = 0# initialize current sum to 0
        max_sum = nums[0]# initialize max sum to the first element of the list
        for i in range(len(nums)):# iterate through the list
            curr_sum += nums[i]# add the current element to the current sum
            if curr_sum > max_sum:# update max sum if current sum is greater
                max_sum = curr_sum # update max sum
            if curr_sum < 0:# reset current sum to 0 if it becomes negative
                curr_sum = 0# reset current sum
        return max_sum# return the maximum subarray sum 
# Example usage:    
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)  # Output: 6
