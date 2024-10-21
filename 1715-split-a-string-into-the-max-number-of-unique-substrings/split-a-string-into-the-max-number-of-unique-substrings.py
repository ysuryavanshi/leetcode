class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        c_set = set()

        def dfs(i):
            if i == len(s): return 0

            ans = 0
            for j in range(i, len(s)):
                sub_string = s[i:j+1]
                if sub_string not in c_set:
                    c_set.add(sub_string)
                    ans = max(ans, 1 + dfs(j + 1))
                    c_set.remove(sub_string)
            return ans
        
        return dfs(0)