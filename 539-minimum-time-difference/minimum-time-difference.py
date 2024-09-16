class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        for i in range(n):
            timePoints[i] = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])

        timePoints.sort()
        ans = 1440 + timePoints[0] - timePoints[-1]

        for i in range(1, n):
            ans = min(ans, (timePoints[i] - timePoints[i-1]))
        return ans