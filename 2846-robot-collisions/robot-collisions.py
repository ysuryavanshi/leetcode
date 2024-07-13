class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        robots = [list(i) for i in zip(positions, healths, directions, range(n))]
        robots.sort()
        i = 1

        while i < n:
            if robots[i-1][2] == 'R' and robots[i][2] == 'L':
                if robots[i-1][1] > robots[i][1]:
                    robots[i-1][1] -= 1
                    _ = robots.pop(i)
                    n -= 1
                elif robots[i-1][1] < robots[i][1]:
                    robots[i][1] -= 1
                    _ = robots.pop(i-1)
                    n -= 1
                    if i > 1: i -= 1
                else:
                    _ = robots.pop(i)
                    _ = robots.pop(i-1)
                    n -= 2
                    if i > 1: i -= 1
            else:
                i += 1
        robots.sort(key=lambda x:x[3])
        return [r[1] for r in robots]