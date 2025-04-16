class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        last_start, last_end = intervals[0]


        for start, end in intervals[1:]:
            if start <= last_end:
                last_end = max(last_end, end)
            else:
                res.append([last_start, last_end])
                last_start = start
                last_end = end

        res.append([last_start, last_end])

        return res
