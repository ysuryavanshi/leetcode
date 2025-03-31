class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k in [len(weights), 1]:
            return 0

        splits = sorted([weights[i - 1] + weights[i] for i in range(1, len(weights))])
        
        return sum(splits[-k + 1:]) - sum(splits[:k - 1])