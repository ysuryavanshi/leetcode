class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        summ = left = res = 0
        
        for right in range(len(nums)):
            summ += nums[right]
            while summ * (right - left + 1) >= k:
                summ -= nums[left]
                left += 1

            res += (right - left + 1)
        
        return res
