class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = set([0])

        for num in nums:
            next_dp = dp.copy()
            for val in dp:
                if (s:= val + num) == target:
                    return True
                next_dp.add(s)
            dp = next_dp

        return False
