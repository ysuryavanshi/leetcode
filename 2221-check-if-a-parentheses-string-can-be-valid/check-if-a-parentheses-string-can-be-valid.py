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
        
        while l_list and un_list and l_list[-1] < un_list[-1]:
            l_list.pop()
            un_list.pop()

        return False if l_list else True
