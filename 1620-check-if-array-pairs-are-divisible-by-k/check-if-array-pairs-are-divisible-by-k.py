class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = [num % k for num in arr]
        mapp = Counter(rem)

        for key in mapp:
            if key == 0 or 2 * key == k:
                if mapp[key] % 2 != 0:
                    return False
            else:
                if mapp[(k - key) % k] != mapp[key]:
                    return False
        return True
