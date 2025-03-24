class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        res, end = meetings[0][0] - 1, meetings[0][1]

        for meeting in meetings:
            if end < meeting[0]:
                res += meeting[0] - (end + 1)
                end = meeting[1]
            elif end == meeting[0]:
                end = meeting[1]
            else:
                end = max(end, meeting[1])

        return res + days - end
