import re
# from word_break import Solution
from solution import Solution

# scenario 1
s = ["applepenapple","catsandog","aaaaaaa"]
wordDict =[ ["apple", "pen"],  ["cats", "dog", "sand", "and", "cat"], ["aaaa","aaa"]]

solution = Solution()
result1= solution.wordBreak(s[0], wordDict[0])
result2= solution.wordBreak(s[1], wordDict[1])
result3= solution.wordBreak(s[2], wordDict[2])
print(result1)  # scenario 1
print(result2)
print(result3)

# scenario 2
