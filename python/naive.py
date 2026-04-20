'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

'''



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # create a DP array
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(0,m-1):
            dp[i+1][0] = dp[i][0] + grid[i+1][0]
        
        for j in range(0,n-1):
            dp[0][j+1] = dp[0][j] + grid[0][j+1]


        for i in range(1,m):
            for j in range(1,n):
                # go down
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
             

        return dp[m-1][n-1]
        