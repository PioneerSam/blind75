'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''


"this is the most naive way of doing things do not ever do this again!"
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     #O(1) extra space O(n) runtime complexity
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
