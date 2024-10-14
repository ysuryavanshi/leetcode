class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def resolve(a, b, operator):
            if operator == '+': return a + b
            if operator == '-': return a - b
            if operator == '*': return a * b
            return int(a / b)

        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(resolve(op1, op2, token))
            else: stack.append(int(token))
        return stack[-1]
