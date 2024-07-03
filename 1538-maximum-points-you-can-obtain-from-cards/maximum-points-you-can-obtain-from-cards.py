import numpy as np

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        prefixsum = list(np.cumsum(cardPoints))
        suffixsum = list(np.cumsum(cardPoints[::-1]))
        ans = ps = ss = 0
        while k > 0:
            if  prefixsum[k-1] - ps > suffixsum[k-1] - ss:
                card = prefixsum.pop(0) - ps
                ps += card
            else:
                card = suffixsum.pop(0) - ss
                ss += card
            ans += card
            k -= 1
        return ans