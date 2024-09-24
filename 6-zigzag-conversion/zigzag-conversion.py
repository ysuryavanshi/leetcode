class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        rows = [''] * numRows
        i = 0
        step = 1

        for c in s:
            rows[i] += c
            if i + step == numRows or i + step == -1:
                step *= -1
            i += step
        
        return ''.join(rows)