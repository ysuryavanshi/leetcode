class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()

        nfactories = []
        for f in factories:
            nfactories.extend([f[0]] * f[1])

        dp = [[-1] * len(nfactories) for _ in range(len(robots))]

        def helper(r, f):
            if r < 0: return 0
            if f < 0: return float('inf')
            if dp[r][f] != -1: return dp[r][f]
            
            include = abs(robots[r] - nfactories[f]) + helper(r - 1, f - 1)
            exclude = helper(r, f - 1)
            dp[r][f] = min(include, exclude)
            return dp[r][f]

        helper(len(robots) - 1, len(nfactories) - 1)
        return dp[-1][-1]