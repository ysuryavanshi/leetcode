class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        res = deque(arr[:k])

        for right in range(k, len(arr)):
            if abs(arr[right] - x) < abs(arr[left] - x):
                left += 1
                _ = res.popleft()
                res.append(arr[right])
        
        return list(res)