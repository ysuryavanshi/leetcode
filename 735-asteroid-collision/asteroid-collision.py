class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack or a > 0:
                stack.append(a)
            else:
                while stack:
                    if stack[-1] < 0:
                        stack.append(a)
                        break
                    
                    if stack[-1] == abs(a):
                        _ = stack.pop()
                        break
                    
                    if stack[-1] < abs(a):
                        stack.pop()
                        if not stack:
                            stack.append(a)
                            break
                    else:
                        break
        return stack
