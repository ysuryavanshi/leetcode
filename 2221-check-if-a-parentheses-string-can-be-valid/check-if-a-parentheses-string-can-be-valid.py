class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        l_list = []
        un_list = []

        for i in range(n):
            if locked[i] == '0':
                un_list.append(i)
            elif s[i] == '(':
                l_list.append(i)
            else:
                if l_list:
                    _ = l_list.pop()
                elif un_list:
                    _ = un_list.pop()
                else:
                    return False
        
        if len(l_list) > len(un_list):
            return False

        for i in reversed(range(len(l_list))):
            if l_list[i] < un_list[-1]:
                _ = l_list.pop(i)
                _ = un_list.pop()

        return False if l_list else True