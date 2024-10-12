class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0

        interval = []
        for left, right in points:
            if not interval:
                interval = [left, right]
            elif interval[1] >= left:
                interval = [left, min(right, interval[1])]
            else:
                ans += 1
                interval = [left, right]
        return ans + 1