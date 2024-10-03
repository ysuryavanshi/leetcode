class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        left = ans = 0
        for i in range(len(s)):
            while s[i] in s_set:
                s_set.discard(s[left])
                left += 1
            s_set.add(s[i])
            ans = max(ans, i - left + 1)
        return ans