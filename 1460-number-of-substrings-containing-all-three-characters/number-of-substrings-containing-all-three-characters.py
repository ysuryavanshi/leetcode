class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        left = 0
        count = {c: 0 for c in 'abc'}

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count.values()):
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res 