class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        top = left = 0
        bot, right = ROWS - 1, COLS - 1

        res = []
        while len(res) < ROWS * COLS:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bot:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bot][i])
                bot -= 1

            if left <= right:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res