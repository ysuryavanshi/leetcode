class Solution:
    def decodeString(self, s: list):
        cnum = '0'
        cstr = ''
        stack = []
        for c in s:
            if c == '[':
                stack.append(cstr)
                stack.append(int(cnum))
                cstr = ''
                cnum = '0'
            elif c == ']':
                num = stack.pop()
                pstr = stack.pop()
                cstr = pstr + num * cstr
            elif c.isdigit():
                cnum += c
            else:
                cstr += c
        return cstr