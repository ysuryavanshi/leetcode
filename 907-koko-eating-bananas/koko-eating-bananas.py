class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(k):
            hours = 0
            for pile in piles:
                hours += pile // k + (1 if pile % k else 0)

                if hours > h:
                    return False
            return True
        
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if can_eat(mid):
                high = mid
            else:
                low = mid + 1
            
        return high


#      lmh        
# 1 2 3 4 5 6 7 8 9
# +++++++----------