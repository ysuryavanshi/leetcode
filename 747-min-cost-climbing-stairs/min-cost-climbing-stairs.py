class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        arr = [0, 0]

        for i in range(2, len(cost)):
            arr.append(min(arr[i - 1] + cost[i], arr[i - 2] + cost [i - 1]))

        return arr[-1]