class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search with index manipulation?
        # don't treat like one long array
        # just do binary search twice, first row then column
        # valid row: current row starts with smaller val and next row starts with too big
        
        # get row
        row = -1
        l = 0
        r = len(matrix) - 1
        while l <= r:
            midpoint = (l + r) // 2
            
            if matrix[midpoint][0] == target:
                return True
            elif matrix[midpoint][0] > target:
                # search left
                r = midpoint - 1
            elif matrix[midpoint][0] < target:
                # check if match
                if (midpoint + 1) == len(matrix) or matrix[midpoint + 1][0] > target:
                    row = midpoint
                    break
                # else search right
                l = midpoint + 1

        # get val; binary search on row
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            midpoint = (l + r) // 2

            if matrix[row][midpoint] == target:
                return True
            elif matrix[row][midpoint] > target:
                # search left
                r = midpoint - 1
            elif matrix[row][midpoint] < target:
                # search right
                l = midpoint + 1

        return False

        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 30
        # row = 2
        # l = 2
        # r = 3
        # midpoint = 2