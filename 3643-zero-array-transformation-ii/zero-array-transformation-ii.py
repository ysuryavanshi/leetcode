class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        def good(target):
            f = [0] * (n + 1)

            for s, e, v in queries[:target]:
                f[s] += v
                f[e + 1] -= v
            
            for i in range(1, n + 1):
                f[i] += f[i - 1]
            
            for i in range(n):
                if nums[i] > f[i]:
                    return False
            return True
        
        left = 0
        right = q + 1

        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        if left == q + 1:
            return -1
        return left