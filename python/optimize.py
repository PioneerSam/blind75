'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

'''




class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_colum_zeros = False
        first_row_zeros = False
        # original zeros
        for i in range(0,m):
            if matrix[i][0] ==0:
                first_colum_zeros = True
                break

        # for rows
        for j in range(0,n):
            if matrix[0][j] ==0:
                first_row_zeros = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # # tackle the first row 
        if first_row_zeros == True:
                for j in range(0,n):
                    matrix[0][j] = 0

        if first_colum_zeros == True:
                for i in range(0,m):
                    matrix[i][0] = 0
                
        
                
