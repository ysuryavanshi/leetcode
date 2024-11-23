class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        ans = [['.'] * m for _ in range(n)]

        for row in range(m):
            i = n - 1
            for col in reversed(range(n)):
                if box[row][col] == '#':
                    ans[i][m - row - 1] = '#'
                    box[row][col] = '.'
                    i -= 1
                elif box[row][col] == '*':
                    ans[col][m - row - 1] = '*'
                    i = col - 1
        return ans