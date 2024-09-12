class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_map = defaultdict(list)
        for i, t in enumerate(temperatures):
            t_map[t].append(i)

        ans = [float('inf')] * (i + 1)
        for i, t in enumerate(temperatures):
            for j in range(t + 1, 101):
                k = bisect.bisect_left(t_map[j], i)
                if k < len(t_map[j]):
                    ans[i] = min(ans[i], t_map[j][k] - i)
            ans[i] = 0 if ans[i] == float('inf') else ans[i]
        return ans