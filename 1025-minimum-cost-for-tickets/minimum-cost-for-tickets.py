class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @cache
        def helper(i):
            if i >= n:
                return 0
            
            one_day = costs[0] + helper(i + 1)

            j = i + 1
            while j < n and days[j] < days[i] + 7: j += 1
            two_day = costs[1] + helper(j)

            while j < n and days[j] < days[i] + 30: j += 1
            thirty_day = costs[2] + helper(j)

            return min(one_day, two_day, thirty_day)
        
        return helper(0)
