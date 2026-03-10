'''

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end_idx = len(nums)-1
        # it is actually a DP....
        memo = {}


        def dfs(idx):
            if idx >= end_idx:
                return True

            if idx in memo:
                return memo[idx]

            maximum_jump = nums[idx]

            if maximum_jump == 0 and idx < end_idx:
                memo[idx] = False
                return False

            for jump in range(1,maximum_jump+1,1):
                if dfs(idx + jump):
                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return False


        return dfs(0)