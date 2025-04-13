class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        i = 0
        res = 0

        for j in range(len(s)):
            if s[j] in count:
                while s[j] in count:
                    count[s[i]] -= 1
                    if count[s[i]] == 0:
                        del count[s[i]]
                    i += 1

            count[s[j]] = 1
            res = max(res, j - i + 1)
        
        return res