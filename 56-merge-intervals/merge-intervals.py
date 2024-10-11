class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()

        for i in intervals:
            if not stack or stack[-1] < i[0]:
                stack.extend(i)
            elif stack[-1] < i[1]:
                _ = stack.pop()
                stack.append(i[1])
        return [stack[r*2:(r+1)*2] for r in range(0,len(stack)//2)] 
