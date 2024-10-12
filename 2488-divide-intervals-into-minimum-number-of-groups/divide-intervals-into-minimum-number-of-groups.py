class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = []
        for left, right in sorted(intervals):
            if groups and groups[0] < left:
                heapq.heappop(groups)
            heapq.heappush(groups, right)
        return len(groups)