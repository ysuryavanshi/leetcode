class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapp = [-2] * 32
        mapp[0] = -1

        max_len = 0
        mask = 0

        for i, char in enumerate(s):
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16
        
            prev = mapp[mask]
            if prev == -2:
                mapp[mask] = i
            else:
                max_len = max(max_len, i - prev)
        
        return max_len