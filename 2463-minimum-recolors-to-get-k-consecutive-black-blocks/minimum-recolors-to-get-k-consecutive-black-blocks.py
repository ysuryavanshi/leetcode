class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[:k])
        left = -1
        res = k - count['B']
        
        for right in range(k, len(blocks)):
            left += 1
            count[blocks[left]] -= 1
            if count[blocks[left]] == 0:
                del count[blocks[left]]
            
            count[blocks[right]] += 1
            res = min(res, k - count['B'])
        
        return res