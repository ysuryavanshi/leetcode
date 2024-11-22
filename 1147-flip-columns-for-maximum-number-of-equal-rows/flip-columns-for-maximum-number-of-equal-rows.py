class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mapp = defaultdict(int)

        for row in matrix:
            if row[0] == 0:
                row = tuple([i ^ 1 for i in row])
            else:
                row = tuple(row)
            mapp[row] += 1
        return max(mapp.values())