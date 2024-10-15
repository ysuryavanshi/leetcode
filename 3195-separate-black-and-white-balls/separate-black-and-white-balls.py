class Solution:
    def minimumSteps(self, s: str) -> int:
        i = ans = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i] == '0': i += 1
            while i < j and s[j] == '1': j -= 1
            ans += j - i
            i += 1
            j -= 1

        return ans