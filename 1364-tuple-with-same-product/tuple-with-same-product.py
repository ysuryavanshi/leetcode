class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        h_map = {}
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in h_map:
                    res += h_map[product] * 8
                    h_map[product] += 1
                else:
                    h_map[product] = 1

        return res