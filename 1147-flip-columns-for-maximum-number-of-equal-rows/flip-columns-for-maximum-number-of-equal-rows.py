class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mapp = Counter()

        for row in matrix:
            pattern = tuple(row) if row[0] == 0 else tuple(i ^ 1 for i in row)
            mapp[pattern] += 1
        return max(mapp.values())