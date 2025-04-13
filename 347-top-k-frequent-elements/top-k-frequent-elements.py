class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)

        for num in nums:
            mapp[num] += 1
        
        frequency_list = [(value, key) for key, value in mapp.items()]
        frequency_list.sort()

        res = []
        while k:
            _, key = frequency_list.pop()
            res.append(key)
            k -= 1
        
        return res