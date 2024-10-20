class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operands = {"!", "&", "|", "t", "f"}
        values = {"t", "f"}
        stack = []

        for c in expression:
            if c == ")":
                val = stack.pop()
                args = set()
                while val in values:
                    args.add(val)
                    val = stack.pop()
                if val == "!":
                    stack.append("f" if "t" in args else "t")
                elif val == "&":
                    stack.append("f" if "f" in args else "t")
                elif val == "|":
                    stack.append("t" if "t" in args else "f")
            elif c in operands:
                stack.append(c)
        return stack[0] == "t"