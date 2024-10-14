class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                op2, op1 = stack.pop(), stack.pop()
                val = eval('%s%s%s'%(op1, token, op2))
                if token == '/':
                    val = floor(val) if val > 0 else ceil(val)
                stack.append(val)
            else: stack.append(token)
        return int(stack[-1])
