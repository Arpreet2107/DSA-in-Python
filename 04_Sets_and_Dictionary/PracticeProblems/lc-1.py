class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)                 # length of the array
        dict1 = {}                    # hash map to store value → index

        for i in range(n):            # traverse each element
            rem = target - nums[i]    # calculate the number needed to reach target

            if rem in dict1:          # check if the required number exists in hashmap
                return [dict1[rem], i] # if yes → return indices of two numbers

            dict1[nums[i]] = i        # otherwise store current number with its index
        return []                     # return empty if no solution found
if __name__ == "__main__":
    nums = [2, 7, 11, 15]       # sample input array
    target = 9                  # target sum
    
    obj = Solution()            # creating object of Solution
    result = obj.twoSum(nums, target)
    
    print("Indices:", result)   # Output → [0, 1]