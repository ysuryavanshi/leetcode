class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        rows = Counter([tuple(g) for g in grid])

        for col in zip(*grid):
            count += rows.get(col, 0)
        return count


with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
            print(Solution().equalPairs(nums),file=f)
exit(0)
