class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        highest = 0
        for i in range(n):
            highest = max(highest, height[i])
            left[i] = highest
        
        highest = 0
        for i in range(n - 1, -1, -1):
            highest = max(highest, height[i])
            right[i] = highest

        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res