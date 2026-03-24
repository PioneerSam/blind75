'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

'''
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
  
        memo = {}
        def dfs(remain):

            best = math.inf
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]

            for i in coins:
                if remain - i >=0:
                   best = min(dfs(remain-i)+1,best)
            
            memo[remain] = best
            return best

        best = dfs(amount)
        if best == math.inf:
            best = -1
        return best


                       
