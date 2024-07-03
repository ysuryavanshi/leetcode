import numpy as np

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        prefixsum = deque(np.cumsum(cardPoints))
        suffixsum = deque(np.cumsum(cardPoints[::-1]))
        ans = ps = ss = 0
        while k > 0:
            if  prefixsum[k-1] - ps > suffixsum[k-1] - ss:
                card = prefixsum.popleft() - ps
                ps += card
            else:
                card = suffixsum.popleft() - ss
                ss += card
            ans += card
            k -= 1
        return ans