class Solution:
    def findTheLongestSubstring(self, s):
        mask_dict, mask, ans = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c == 'a': mask ^= 1
            elif c == 'e': mask ^= 1 << 1
            elif c == 'i': mask ^= 1 << 2
            elif c == 'o': mask ^= 1 << 3
            elif c == 'u': mask ^= 1 << 4
            if (diff := i-mask_dict.setdefault(mask, i)) > ans:ans = diff
        return ans