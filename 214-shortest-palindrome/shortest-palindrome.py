class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix, base = 0, 0, 29
        last_index = 0
        power = 1

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1
            prefix = ((prefix * base) + char)

            suffix = (suffix + char * power)
            power = (power * base)

            if prefix == suffix:
                last_index = i

        return s[last_index + 1:][::-1] + s