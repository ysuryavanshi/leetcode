class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        size = len(cardPoints)
        left, right = k-1, size-1

        current_pick = sum(cardPoints[:k])
        max_points = current_pick

        for _ in range(k):
            current_pick += cardPoints[right] - cardPoints[left]
            max_points = max(max_points, current_pick)
            left, right = left - 1, right - 1
        return max_points