class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def helper(c):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= c:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k
        
        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        
        return left