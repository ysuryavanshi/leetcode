class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        ans = []
        for i in range(len(expression)):
            if expression[i] in '+*-':
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i+1:])
                for j in l:
                    for k in r:
                        if expression[i] == '+':
                            ans.append(j + k)
                        elif expression[i] == '-':
                            ans.append(j - k)
                        elif expression[i] == '*':
                            ans.append(j * k)
        return ans