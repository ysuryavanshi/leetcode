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

        def backtrack(combo, n_digits):
            if not n_digits:
                ans.append(combo)
            else:
                for l in phone_map[n_digits[0]]:
                    backtrack(combo + l, n_digits[1:])
        
        ans = []
        backtrack('', digits)
        return ans