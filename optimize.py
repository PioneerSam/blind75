'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplet = set()
        
        for i in range(0,n):
            if nums[i] == nums[i-1] and i>0: # skip duplicate numbers
                continue
            target_sum = 0 - nums[i]
            seen = {}
             # ok now we use the two sum methods hashmap O(1) this is a two sum problem
            for j in range(i+1,n):
                value = nums[j]
                if i != j:
                    need = target_sum - value
                    if need in seen:
                        to_add = [nums[seen[need]],nums[i],nums[j]]
                        to_add.sort()
                        to_add = tuple(to_add)
                        if to_add not in triplet:
                            triplet.add(to_add)

                    seen[value] = j

            
        return list(triplet)
