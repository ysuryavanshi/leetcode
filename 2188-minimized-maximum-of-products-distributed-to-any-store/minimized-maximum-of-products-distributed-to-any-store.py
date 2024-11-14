class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(k):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / k)
            return stores <= n

        high, low = max(quantities), 1
        while low < high:
            mid = (low + high) // 2
            if can_distribute(mid):
                high = mid
            else:
                low = mid + 1
        return low