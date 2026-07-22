class Solution:
    # iterate each item in matrix:
    #   if 0 found:
    #       mark corresponding item in first row and first column as 0
    #
    # second pass only over first row:
    #   if 0 found:
    #       zero out entire row
    #
    # third pass, same idea as above but with column
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        