'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

'''



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # I can actually just keep track of which column and rows need to set zero and then go do it lol

        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for i in range(m):
            for j in cols:
                matrix[i][j] = 0


                       
