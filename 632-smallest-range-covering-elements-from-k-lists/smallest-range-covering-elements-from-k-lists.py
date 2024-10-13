class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cur_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])
        ans = [float('-inf'), float('inf')]
        while heap:
            cur_min, list_idx, i = heapq.heappop(heap)
            if (cur_max - cur_min < ans[1] - ans[0]) or ((cur_max - cur_min == ans[1] - ans[0]) and cur_min < ans[0]):
                ans = [cur_min, cur_max]
            if i + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][i + 1]
                heapq.heappush(heap, (nxt, list_idx, i + 1))
                cur_max = max(cur_max, nxt)
            else:
                break
        return ans