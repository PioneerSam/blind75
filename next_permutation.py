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
        from itertools import permutations

       
        import numpy as np
        nums_np = np.array(nums).reshape(1,3)
        iterator = permutations(list(np.squeeze(np.sort(nums_np))))

       
        iterator_list = np.array(list(iterator))

        n = iterator_list.shape[0]

        # print("the shape of nums_np_np is:", nums_np.shape)
        # print("nums_np is:",nums_np)

        # print("the shape of iterator is: ", iterator_list.shape)
        print("itertaor", iterator_list)
        print("nums_np:", nums_np)
        cnt = 0
        for element in iterator_list:
            print("element: ", element)

            print("nums_np[0]", nums_np[0])

            l = len(element)
            print("the length of element is: ",l)

            equal = True
            for i in range(0,l):
                if element[i] !=nums_np[0][i]:
                    equal = False
                    break

            if equal:
                print("the index when equal = True", cnt)

                for j in range(0,l,1):
                    if cnt == (len(iterator_list)-1):
                        nums[j] = int(iterator_list[0][j])
                    else:
                        nums[j] = int(iterator_list[cnt+1][j])

            cnt+=1




