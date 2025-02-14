

from typing import List

#Inplace changes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_col_zero = 1
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0  # Mark the first cell of the row
                    if column != 0:
                        matrix[0][column] = 0   # Mark the first cell of the column
                    else:
                        row_col_zero = 0    # Indicate that column 0 must be zeroed

        # Update the matrix based on markers (excluding the first row and column for now)
        #starting for 1 because we will update the zero index separately 

        for row in range(1,len(matrix)):
            for column in range(1,len(matrix[0])):

                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0

        # Zero out the first row if necessary
        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        # Zero out the first column if necessary
        if row_col_zero == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        



#this is the an extra arrays issue 
#O(N*M) time complexity
#Space Complexity: O(N) + O(M)
'''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x_range = [0] * len(matrix)
        y_range = [0] * len(matrix[0])
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    x_range[row] = 1
                    y_range[column] = 1
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if x_range[row] or y_range[column]:
                    matrix[row][column] = 0
        #return matrix
'''                


matrix = [[1,1,1],[1,0,1],[1,1,1]]
a = Solution()
a.setZeroes(matrix)        
print(matrix)