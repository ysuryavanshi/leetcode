class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0]
        suffix = [0]
        for i in range(0, n-1):
            prefix.append(nums[i] + prefix[-1])
        for i in range(n-1, 0, -1):
            suffix.insert(0, nums[i] + suffix[0])
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        return -1