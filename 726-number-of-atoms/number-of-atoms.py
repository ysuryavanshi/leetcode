class Solution:
    def countOfAtoms(self, formula: str) -> str:

        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                top = stack.pop()
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * multiplicity
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] += count
    
        final_count = stack.pop()
        sorted_elements = sorted(final_count.items())
        
        result = []
        for element, count in sorted_elements:
            if count > 1:
                result.append(f"{element}{count}")
            else:
                result.append(element)
        
        return "".join(result)
        