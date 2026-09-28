class Solution:
    def isValid(self, s: str) -> bool:
        # Can there be letters besides the parentheses

        stack = []
        matches = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        for letter in s:
            if letter in matches:
                stack.append(letter)
            else:
                if stack and matches[stack[-1]] == letter:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0