class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        mi = min(nums)
        ma = max(nums)
        ans = []

        for n in range(mi, ma + 1):
            ans.extend([n] * c[n])
        return ans