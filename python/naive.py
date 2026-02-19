'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows should be columns
        # first row is the last column and first column in reverse is the first row

        # I can mirror across the diagonal and reverse the rows lol
        # lets mirror it i,j = j,i easy
        numRows = len(matrix)
        numCols = len(matrix[0])
        print("numrows",numRows)
        print("numcols",numCols)
        for i in range(numRows):
            for j in range(i,numCols):
                print("(i,j)",(i,j))
                temp_ij = matrix[i][j]
                temp_ji = matrix[j][i]

                # swap 
                matrix[i][j] = temp_ji
                # print("pair is (i,j) --> (j,i)",temp_ij,temp_ji)
                matrix[j][i] = temp_ij

        print(matrix)

        # now reverse each rows
        for i in range(numRows):
            matrix[i].reverse()

        return matrix
        