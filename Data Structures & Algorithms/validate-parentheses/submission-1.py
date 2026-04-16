class Solution:
    def isValid(self, s: str) -> bool:
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('()', '')
    #         s = s.replace('{}', '')
    #         s = s.replace('[]', '')

    #     return s == ""
        stack = []

        closetoopen = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False

        
    