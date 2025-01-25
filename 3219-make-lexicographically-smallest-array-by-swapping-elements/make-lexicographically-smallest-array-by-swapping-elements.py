class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        mapping = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            mapping[n] = len(groups) - 1
        
        res = []
        for n in nums:
            idx = mapping[n]
            res.append(groups[idx].popleft())
        
        return res
