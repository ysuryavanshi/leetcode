class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_negative = 0
        values = []
        heapify(values)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if val < 0: count_negative += 1
                heapq.heappush(values, abs(matrix[i][j]))
        
        ans = -heapq.heappop(values) if count_negative % 2 == 1 else 0        
        while values:
            ans += heapq.heappop(values)
        return ans