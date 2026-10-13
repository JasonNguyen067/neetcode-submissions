class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {
            "[":"]",
            "{":"}",
            "(":")"
        }

        for val in s:
            if val in pairs:
                stack.append(val)
            elif stack and pairs[stack[-1]] == val:
                stack.pop()
            else:
                return False

        return len(stack) == 0