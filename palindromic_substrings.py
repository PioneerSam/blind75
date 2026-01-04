'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n>1000 or n<1:
            return 0
        
        # cnt = 0 # beacuse every character counts
        # # and then you bild substrings and check lol
        # # ok I dont know the length it will be expenential again if I checked every combination lol
        # # here is a hint if a substring is already a palindromic string
        # # then there is a chance another string could be just by one idx 
        # mid_idx = len(s) //2
        # print("mid_idx is: ", mid_idx)
        # left_offset = 0
        # right_offset = 0

        # go_left = True

        # while ((mid_idx - left_offset >= 0) or (mid_idx + right_offset < len(s))):
        #     if (go_left):
        #         if (mid_idx - left_offset >= 0):
        #             left_offset += 1
        #             cnt += 1
        #     else:
        #         if (mid_idx + right_offset < cnt):
        #             right_offset += 1
        #             cnt += 1
            
        #     substring = s[mid_idx-left_offset:mid_idx+right_offset]
        #     if len(substring) == 1:
        #         continue
        #     print("------------")
        #     print("left_idx: ", mid_idx-left_offset)
        #     print("right_idx: ", mid_idx+right_offset)
        #     print("substring to check: ", substring)
        #     check = self.check_palindrome(substring)
        #     print("result: ",check)

        #     if check:
        #         cnt += 1

        #     go_left = not go_left
        
        # return cnt

        # think about how many even centers and odd centers
        cnt = 0

        # I grow a palidrome at each index that is the naive method
        for idx in range(0,n,1):
            # for this index I need to grow both sides and see if it is one l
            # ok there is an even and odd intilization
            # for odd center
    
            left_idx = right_idx = idx
            cnt += 1
            while left_idx> 0 and right_idx < n-1:
                if(s[left_idx-1] == s[right_idx+1]):
                    cnt +=1
                    left_idx -= 1
                    right_idx +=1 
                else:
                    break
            
            if idx+1 != n:
                if s[idx] == s[idx+1]: #even center
                    left_idx = idx
                    right_idx = idx+1
                    cnt+=1
        
                while left_idx> 0 and right_idx < n-1:
                    if(s[left_idx-1] == s[right_idx+1]):
                        cnt +=1
                        left_idx -= 1
                        right_idx +=1 
                    else:
                        break
            
        return cnt



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

