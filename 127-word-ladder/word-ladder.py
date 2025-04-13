class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        res = 0
        q = deque([(beginWord, 0)])
        
        while q:
            for _ in range(len(q)):
                word, step = q.popleft()

                if word == endWord:
                    return step + 1

                for i in range(len(word)):
                    word = list(word)

                    for c in range(1, 27):
                        temp = word[i]
                        word[i] = chr(96 + c)

                        if ''.join(word) in wordList:
                            wordList.remove(''.join(word))
                            q.append((''.join(word), step + 1))

                        word[i] = temp

        return 0