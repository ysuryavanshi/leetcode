class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        series = [0]

        for d in differences:
            series.append(series[-1] + d)
        
        res = upper - lower + 1 - (max(series) - min(series))
        return res if res > 0 else 0


# 3 4 1 5

# -3 0 -4 1 2 0

# 0 1 -2 2
# 6 - 1 + 1 - range = 2

# 0 3 -1 4 5 3
# range = 6
# 5 + 4 + 1 - 6 = 4

# 0 4 -3 -1
# range = 7
# 6 -3 + 1 - 7