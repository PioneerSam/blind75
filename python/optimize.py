'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
  
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for i in range(1,len(dp),1):
            for coin_value in coins:
                if i - coin_value == 0:
                    dp[i] = min(dp[i],dp[i-coin_value] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return 0
                
