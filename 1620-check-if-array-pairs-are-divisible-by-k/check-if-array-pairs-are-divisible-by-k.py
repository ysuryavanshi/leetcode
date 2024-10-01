class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mapp = collections.defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = k - (num % k)
            if key in mapp and mapp[key] >= 1:
                count += 1
                mapp[key] -= 1
            else:
                mapp[(num % k) or k] += 1
        return count == len(arr) // 2
        
