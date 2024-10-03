class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0: return 0

        ans = len(nums)
        cur_sum = 0
        rem_to_idx = {0: -1}
        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - target + p) % p
            if prefix in rem_to_idx:
                length = i - rem_to_idx[prefix]
                ans = min(ans, length)
            rem_to_idx[cur_sum] = i

        return -1 if ans == len(nums) else ans