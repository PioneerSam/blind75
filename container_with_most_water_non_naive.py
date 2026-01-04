'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # oki find area easy
        max = 0 

        n = len(height)

        # ok cant start in the middle lol

        lidx = 0
        ridx = n-1

        max = self.calculate_area(lidx,ridx,height)

        while lidx != ridx:
            # move an idx if I can get better height
            current_l_height = height[lidx]
            current_r_right = height[ridx]

            # next_l_height = height[lidx+1]
            # next_r_height = height[ridx-1]

            if current_l_height < current_r_right:
                lidx += 1
            else:
                ridx -= 1

            current_area = self.calculate_area(lidx,ridx,height)

            if current_area > max:
                max = current_area

        
        return max

        

        
            


    def calculate_area(self,idx1,idx2,height):
        width = idx2 - idx1
        height1 = height[idx1]
        height2 = height[idx2]

        height_final = min(height1,height2)

        return width*height_final


        



    # def check_palindrome(self,s):
    #     # import numpy as np
    #     if len(s)>1000 or len(s)<1:
    #         return False
        
    #     n = len(s)
    #     # I think I can use a stack first in last out and check characters (not really)
    #     mid_idx = n//2 # ok if it is 3 mid idx is 1

    #     for idx in range(0,mid_idx,1):
    #         if s[idx] != s[n-idx-1]:
    #             return False
        
    #     return True



test = Solution()

string = "abc"

cnt = test.countSubstrings(string)

print(cnt)

# print(test.check_palindrome(string))

