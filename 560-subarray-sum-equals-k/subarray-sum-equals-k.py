class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0: 1}
        prefix_sum = res = 0

        for n in nums:
            prefix_sum += n
            res += hmap.get(prefix_sum - k, 0)
            hmap[prefix_sum] = 1 + hmap.get(prefix_sum, 0)
        
        return res
