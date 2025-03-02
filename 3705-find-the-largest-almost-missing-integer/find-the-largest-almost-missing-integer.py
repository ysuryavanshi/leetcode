class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)

        if n == k:
            return max(nums)
        
        for i in range(n - k + 1):
            for j in range(i, i + k):
                freq[nums[j]] += 1
            
        res = -1
        for num, count in freq.items():
            if count == 1:
                res = max(res, num)
        
        return res