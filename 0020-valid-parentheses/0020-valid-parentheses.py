# 20. Valid Parenthese

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == "]":
                if stack.pop() != "[":
                    return False
            elif i == ")":
                if stack.pop() != "(":
                    return False
            else:
                if stack.pop() != "{":
                    return False
        if len(stack) != 0:
            return False
        return True


print(Solution().isValid("(("))
