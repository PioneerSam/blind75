'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        d = len(word)

        visited = [[False] * m for _ in range(n)]

        def dfs(i,j,idx):
            if not (0<=i<n and 0<=j<m):
                return False
            
            if visited[i][j]:
                return False
            
            cur_letter = word[idx]
            if(board[i][j] == cur_letter):
                if idx == d-1:
                    return True
                visited[i][j] = True
                dir_vec = [(1,0),(0,1),(-1,0),(0,-1)]
                
                for dr,dc in dir_vec:
                    nr = i + dr
                    nc = j + dc
                    if (0<=nr<n and 0<=nc<m) and idx + 1 <d:
                        if dfs(nr,nc,idx+1):
                            return True
                visited[i][j] = False    
                return False
            else:
                return False
         
        for i in range(n):
            for j in range(m):
                ans = dfs(i,j,0)
                if ans:
                    return True
        return False

    
                
        



                    
                
