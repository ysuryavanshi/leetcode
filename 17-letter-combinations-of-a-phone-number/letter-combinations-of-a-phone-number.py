class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, chars):
            nonlocal res
            if i == len(digits):
                if chars:
                    res.append(chars)
                return
            
            for letters in keyboard[digits[i]]:
                for l in letters:
                    backtrack(i+1, chars + l)

        backtrack(0, '')
        return res
