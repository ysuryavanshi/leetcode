class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for args in zip(*strs):
            if len(set(args)) == 1:
                res += args[0]
            else:
                break
        
        return res