class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        nums = [str(n) for n in nums]

        ans = []
        for k, trim in queries:
            t_nums = [n[-trim:] for n in nums]
            ans.append(sorted([(b,i) for i, b in enumerate(t_nums)])[k-1][1])
        return ans
