class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        start = intervals[0][0]
        ans = 0

        for i in range(len(intervals)):
            if intervals[i][0] >= start:
                start = intervals[i][1]
            else:
                ans += 1
        return ans