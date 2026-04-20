'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

'''


# top down
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = {}
        def dfs(i,j):
            if i == 0:
                accum = sum(grid[0][:j+1])
                memo[(i,j)] = accum
                return accum
            if j == 0:
                accum = 0
                for index in range(0,i+1):
                    accum += grid[index][0]
                memo[(i,j)] = accum
                return accum
            # if i == j == 0:
            #     return grid[0][0]
            

            if (i,j) in memo:
                return memo[(i,j)]
            

            ans = grid[i][j] + min(dfs(i-1,j),dfs(i,j-1))
            memo[(i,j)] = ans
            return ans
        

        return dfs(m-1,n-1)