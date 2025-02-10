class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)

        start_row = -1
        for row in range(ROWS):
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                start_row = row - 1
                break
        
        return target in matrix[start_row]