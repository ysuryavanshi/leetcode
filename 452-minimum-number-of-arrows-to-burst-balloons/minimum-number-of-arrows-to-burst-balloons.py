class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0

        window = None
        for i in range(len(points)):
            if not window: window = points[i]
            elif points[i][0] <= window[1]:
                window[0] = points[i][0]
                if points[i][1] < window[1]: window[1] = points[i][1]
            else:
                ans += 1
                window = points[i]

        if window: ans+= 1
        return ans