class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = [[-1] * n for _ in range(m)]

        for w in walls:
            ans[w[0]][w[1]] = 'W'

        for g in guards:
            ans[g[0]][g[1]] = 'G'
        
        for g in guards:
            for d in directions:
                cur = [g[0] + d[0], g[1] + d[1]]
                while 0 <= cur[0] < m and 0 <= cur[1] < n:
                    if ans[cur[0]][cur[1]] in [-1, 1]:
                        ans[cur[0]][cur[1]] = 1
                        cur = [cur[0] + d[0], cur[1] + d[1]]
                    else:
                        break

        return sum([sum([1 for c in r if c == -1]) for r in ans])