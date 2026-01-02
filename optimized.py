class Solution:
    def wordBreak(self, s, wordDict):
        if not s:
            return False

        wordSet = set(wordDict)

        minwordlen = min(len(word) for word in wordSet)
        maxwordlen = max(len(word) for word in wordSet)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty prefix is valid

        for i in range(n):
            if not dp[i]:
                continue  # unreachable state, skip

            for length in range(minwordlen, maxwordlen + 1):
                j = i + length
                if j > n:
                    break

                if s[i:j] in wordSet:
                    dp[j] = True

        return dp[n]
