'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory
'''


"this is the most naive way of doing things do not ever do this again!"
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums_np in-place instead.
        """
        # greedy algo
        assert len(nums) <= 100

        n = len(nums)

        lowest = 1000
        lowest_id = None

        idx = n-1
        while nums[idx] < nums[idx-1]:

            idx-=1

        print("The pivot index is: ",idx)
        # for idx in range(n,-1,-1):
        #     if nums[idx] < nums[idx-1]:
        #         if nums[idx] < lowest:
        #             lowest = nums[idx]
        #             lowest_id = idx
        #             continue
        #         else:
        #             if nums[idx] < lowest:
        #                 nums[lowest_id] = nums[idx]
        #                 nums[idx] = lowest
        #             else: 
        #                 temp = nums[idx-1]
        #                 nums[idx-1] = nums[idx]
        #                 nums[idx] = temp

        #                 # need to sort from idx to n
        #                 nums_slice = nums[idx:n]
        #                 sorted_num_slice = sorted(nums_slice)

        #                 for j in range(0,len(nums_slice),1):
        #                     nums[idx+j] = sorted_num_slice[j]
        #     if idx == 0:
        #         nums = nums.reverse()

        




