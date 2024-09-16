class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        for i in range(n):
            h, m = timePoints[i].split(':')
            timePoints[i] = int(h) * 60 + int(m)

        ans = 720
        timePoints.sort()
        for i in range(n):
            if (diff := abs(timePoints[i] - timePoints[i - 1])) > 720:
                diff = 1440 - diff
            ans = min(ans, diff)
        return ans