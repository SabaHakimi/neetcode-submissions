class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {'(', '[', '{'}
        brackets = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
                        
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif stack and stack[-1] == brackets[bracket]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        return False

            