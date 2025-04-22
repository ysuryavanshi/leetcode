class Trie:
    def __init__(self, wordDict):
        self.words = {}
        for word in wordDict:
            self.__addWord(word)

    def __addWord(self, word):
        head = self.words
        for c in word:
            if c not in head:
                head[c] = {}
            head = head[c]
        head['*'] = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie(wordDict)
        res = []
        
        def dfs(i, node, word, words):
            if i == len(s):
                if not word:
                    res.append(' '.join(words))
                return
            
            if s[i] not in node:
                return
            
            word += s[i]
            node = node[s[i]]

            if '*' in node:
                dfs(i + 1, trie.words, '', words + [word])
            
            dfs(i + 1, node, word, words)

        dfs(0, trie.words, '', [])
        return res
