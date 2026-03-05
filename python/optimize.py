'''

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        positive_check = False
        for i in nums:
            if i > 0:
                positive_check = True
                break
        if positive_check == False:
            return max(nums)
        if len(nums) == 1:
            return nums[0]
        nums_copy = nums.copy()
        shave_check = True
        while shave_check == True:
            shave_check = False
            z = 0
            for i in range(len(nums_copy)):
                z = z + nums_copy[i]
                if z < 0:
                    nums_copy = nums_copy[i+1:]
                    shave_check = True
                    
                    print(nums_copy)
                    break
            z = 0
            for i in range(len(nums_copy)-1,-1,-1):
                #  print(i)
                z += nums_copy[i]

                if z < 0:
                    shave_check = True
                    nums_copy = nums_copy[:i]
                    
                    print(nums_copy)
                    break
        return(sum(nums_copy))