class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        n = len(nums)//2
        for key, value in d.items():
            if value > n:
                return key
        return