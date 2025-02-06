class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        h_map = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                h_map[nums[i] * nums[j]] += 1
        
        res = 0
        for count in h_map.values():
            if count > 1:
                res += count * (count - 1) // 2

        return res * 8