class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def bits_update(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            result = 0
            for i in range(32):
                if bits[i]:
                    result += (1 << i)
            return result

        bits = [0] * 32
        l, ans = 0, float('inf')

        for r in range(len(nums)):
            bits_update(bits, nums[r], 1)
            
            cur_or = bits_to_int(bits)
            
            while l <= r and cur_or >= k:
                ans = min(ans, r - l + 1)
                bits_update(bits, nums[l], -1)
                cur_or = bits_to_int(bits)
                l += 1
        
        return -1 if ans == float('inf') else ans