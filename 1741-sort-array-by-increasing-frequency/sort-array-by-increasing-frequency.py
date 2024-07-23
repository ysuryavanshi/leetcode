class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        val = Counter(nums).most_common()[::-1]
        val.sort(reverse=True)
        val.sort(key=lambda x: x[1])
        for x, y in val:
            ans.extend([x]*y)
        return ans