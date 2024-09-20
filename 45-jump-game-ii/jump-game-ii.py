class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [0] + [float(inf)] * (n - 1)
        for i, num in enumerate(nums):
            j = 1
            while i + j < n and j <= num:
                if jumps[i + j] > jumps[i] + 1:
                    jumps[i + j] = jumps[i] + 1
                j += 1
        print(jumps)
        return jumps[-1]