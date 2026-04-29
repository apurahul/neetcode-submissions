class Solution:
    def isValid(self, s: str) -> bool:
        bracs = {')': '(', '}':'{', ']':'['}

        stack = []

        for c in s:
            if c in bracs:
                if stack and stack[-1] == bracs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True


        