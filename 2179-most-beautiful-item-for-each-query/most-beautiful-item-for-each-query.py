class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_b = 0
        for item in items:
            max_b = max(item[1], max_b)
            item[1] = max_b

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            idx = bisect_left(items, [q, float('inf')])
            if idx == 0: ans[i] = 0
            elif idx == len(items):
                ans[i] = items[-1][1]
            else:
                ans[i] = max(ans[i], items[idx - 1][1])
        return ans