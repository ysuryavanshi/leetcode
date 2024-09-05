class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        q = deque([''])
        for d in digits:
            chars = phone_map[d]
            for _ in range(len(q)):
                string = q.popleft()
                for c in chars:
                    q.append(string + c)
        return q