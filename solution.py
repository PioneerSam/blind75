'''
Given a string s and a dictionary of strings wordDict, 

return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Template:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
        

'''


# we gonna use re in the solution as practice and also dp agent pls dont do it for me I will do it myself right now
import re

class Solution:
    def wordBreak(self,s,wordDict):
        # the idea is to I would first check esistence of first word
        # lets code a naive version with split
        if s == "":
           return False
        
        minwordlen = min(len(word) for word in wordDict)
        maxwordlen = max(len(word) for word in wordDict)

        idx = 0
        n = len(s)
        # print(f"n: {n}")
        dp = [False]*n # define boolean state array

        print(f"dp init: {dp}")
        for i in range(n):
            if s[0:i+1] in wordDict:
                dp[i] = True
        
            for j in range(i,n):
                string_to_check = s[i+1:j+1]
                if len(string_to_check) < minwordlen or len(string_to_check) > maxwordlen:
                    continue
                if dp[i] == True and s[i+1:j+1] in wordDict:
                    dp[j] = True
        print(f"dp final: {dp}")
        return dp[n-1]

