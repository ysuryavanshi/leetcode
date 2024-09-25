class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.score += 1

        ans = []
        for word in words:
            current = root
            score = 0
            for char in word:
                current = current.children[char]
                score += current.score
            ans.append(score)
        
        return ans