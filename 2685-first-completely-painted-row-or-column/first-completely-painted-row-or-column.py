class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        mapping = {}
        f_c = [0] * COLS
        f_r = [0] * ROWS
        for r in range(ROWS):
            for c in range(COLS):
                mapping[mat[r][c]] = (r, c)

        for idx, val in enumerate(arr):
            r, c = mapping[val]
            f_c[c] += 1
            f_r[r] += 1

            if f_c[c] == ROWS or f_r[r] == COLS:
                return idx
