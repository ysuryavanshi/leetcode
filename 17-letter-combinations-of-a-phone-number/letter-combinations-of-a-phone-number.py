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
            "9": "wxyz"
        }
        res = []

        def backtrack(i, string):
            if i == len(digits):
                if string:
                    res.append(string)
                return
            
            for c in keyboard[digits[i]]:
                backtrack(i + 1, string + c)

        backtrack(0, '')
        return res
