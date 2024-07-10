class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                prefix += c[0]
            else:
                break
        return prefix