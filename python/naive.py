'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # start any letter and try to dfs 
        current = ''
        # do a boolean grid of visted 
        m = len(board)
        n = len(board[0])
        d = len(word)

        if m ==n and m == 1:
            return board[m-1][n-1] == word

   
        # print(visited)
        current_idx = 0
        first_letter = word[current_idx]

        from collections import deque

        # Create a deque instance
        q = deque()
        dir_vec = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]

                if board[i][j] == first_letter:
                    # print("starting expanding at node",(i,j))
                    if d == 1:
                        return True
                    
                    if current_idx < d:
                        current_idx = 1
                    # visited[i][j] = True
                    q.append((i,j,current_idx,{(i,j)}))
                
                while q:
                    current = q.popleft()
                    r = current[0]
                    c = current[1]
                    current_idx = current[2]
                    # print("I am at",(r,c))
                    current_letter = word[current_idx]
                    # print("matching index word:", current_idx)
                    # print("matching letter:", current_letter)
                    path = current[3]

                    for dr,dc in dir_vec:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < m and 0 <= nc < n:
                            if (nr,nc) not in path and board[nr][nc] == current_letter:
                                if current_idx == d-1:
                                    return True
                                else:
                                    next_idx = current_idx + 1
                                # print("----nr,nc-----",(nr,nc))
                                new_path = path.copy()
                                new_path.add((nr,nc))
                                # visited[nr][nc] = True
                                q.append((nr,nc,next_idx,new_path))

        return False

                
# [["A","B","C","E"],
#  ["S","F","E","S"],
#  ["A","D","E","E"]]
                

                       
