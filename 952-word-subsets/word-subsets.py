class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = defaultdict(int)
        for word in words2:
            cur = Counter(word)
            for c in cur:
                count[c] = max(count[c], cur[c])

        ans = []
        for word in words1:
            cur = Counter(word)
            if all(cur[c] >= count[c] for c in count):
                ans.append(word)
        return ans