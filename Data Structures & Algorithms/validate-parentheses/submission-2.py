class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for letter in s:
            if letter in pairs:
                stack.append(letter)
            else:
                if stack and pairs[stack[-1]] == letter:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0

