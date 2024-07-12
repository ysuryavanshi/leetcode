class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(string, substring):
            count = 0
            stack = deque()
            for s in string:
                if s in 'ab':
                    if stack and stack[-1] == substring[0] and s == substring[1]:
                        count += 1
                        _ = stack.pop()
                    else: stack.append(s)
                else: stack.append(s)
            return ''.join(stack), count

        if x > y:
            s, count = helper(s, 'ab')
            _, count1 = helper(s, 'ba')
        else:
            s, count1 = helper(s, 'ba')
            _, count = helper(s, 'ab')
        return x * count + y * count1