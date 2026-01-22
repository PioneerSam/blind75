'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplet = set()
        for i in range(0,n):
            for j in range(0,n):
                if i == j:
                    continue
                for k in range(0,n):
                    if j==k or i==k:
                        continue

                    if nums[i]+nums[j]+nums[k] == 0:
                        to_add = [nums[i],nums[j],nums[k]]
                        to_add.sort()
                        to_add = tuple(to_add)
                        if to_add not in triplet:
                            triplet.add(to_add)
                
        return list(triplet)
            
