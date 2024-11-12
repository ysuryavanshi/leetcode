class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_b = 0
        for item in items:
            max_b = max(item[1], max_b)
            item[1] = max_b

        ans = []
        for i, q in enumerate(queries):
            idx = bisect_left(items, [q, float('inf')])
            if idx == 0: ans.append(0)
            else: ans.append(items[idx - 1][1])
        return ans