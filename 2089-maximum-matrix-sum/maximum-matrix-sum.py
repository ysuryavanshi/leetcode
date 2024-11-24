class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = count_negative = 0
        min_value = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    count_negative += 1
                
                if abs(matrix[i][j]) < min_value:
                    min_value = abs(matrix[i][j])
                ans += abs(matrix[i][j])
        
        return ans - (2 * min_value) if count_negative % 2 == 1 else ans