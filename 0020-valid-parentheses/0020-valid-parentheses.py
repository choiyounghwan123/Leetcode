# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []
        
        for parenthese in s:
            if parenthese in [")","]","}"]:
                if not stack:
                    return False
            if parenthese == "(":
                stack.append(parenthese)
            elif parenthese == "[":
                stack.append(parenthese)
            elif parenthese == "{":
                stack.append(parenthese)
            elif stack and parenthese == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif stack and parenthese == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            else:
                if stack and stack[-1] != "{":
                    return False
                stack.pop()
        if stack:
            return False
        return True

solution = Solution()
print(solution.isValid(s = "()"))