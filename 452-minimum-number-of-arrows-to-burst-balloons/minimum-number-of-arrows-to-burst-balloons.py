class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 1

        end = points[0][1]

        for balloon in points[1:]:
            if balloon[0] > end:
                ans += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])
        return ans