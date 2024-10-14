class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def fsum(a, b): return a + b
        def fsub(a, b): return a - b
        def fmul(a, b): return a * b
        def fdiv(a, b): x = a/b; return ceil(x) if x < 0 else floor(x)

        stack = []
        operators = {'+': fsum, '-': fsub, '*': fmul, '/': fdiv}

        for token in tokens:
            if token in operators:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(operators[token](op1, op2))
            else: stack.append(int(token))
        return stack[-1]
