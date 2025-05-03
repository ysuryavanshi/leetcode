class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        res, len_res = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < len_res:
                    res = [l, r]
                    len_res = (r - l + 1)
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if len_res != float('inf') else ''