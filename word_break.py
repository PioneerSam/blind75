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


class Solution:
    def wordBreak(self,s,wordDict):
        # the idea is to I would first check esistence of first word
        # lets code a naive version with split

        idx = 0
        n = len(s)
        # print(f"n: {n}")
        # assert n >= 1 and n <= 300
        # assert len(wordDict) >= 1 and len(wordDict) <= 1000
        # assert all(len(word) >= 1 and len(word) <= 20 for word in wordDict)

        # for i in range(n):
        #     substring = s[idx:i+1]
        #     print(f"substring: {substring}")

        #     if substring in wordDict:
        #         remaining = s[i+1:]
        #         print(f"found word: {substring}, remaining: {remaining}")
        #         idx = i+1

        #         if remaining in wordDict:
        #             return True
                
        # return idx == n
        # ok this doesnt work because it only checks for first word and it breaks if there is many first word matches
        # and one of them leads to the breakdown of the rest of the string so need to try all of them
        
        # new idea here well the dp solution will be in solution.py
        # we do naive here
        
        # I think I can write is recursively
        if s == "":
           return True
        for word in wordDict:
            if s.startswith(word):
                suffix = s[len(word):]
                # print(f"word: {word}, suffix: {suffix}")
                if self.wordBreak(suffix, wordDict):
                    return True
        return False
    
    # note to myself this works but it is exponential time complexity because of the recursion and overlapping subproblems
    # so we will implement dp version in solution.py
    



      
                
