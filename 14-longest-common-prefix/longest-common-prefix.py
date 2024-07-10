class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(min(strs, key=len))
        i = 0
        match = True
        while i < m and match:
            val = ''
            for s in strs:
                if not val: val = s[i]
                else:  match = val == s[i]
                if match == False: break
            if match: i += 1
        return strs[0][:i]

