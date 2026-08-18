class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combinations = {
            '{':'}',
            '[':']',
            '(':')'
        }

        for letter in s:
            if letter in combinations:
                stack.append(letter)
            else:
                if stack and combinations[stack[-1]] == letter:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

        # Time complexity is O(N)
        # space complexity O(N) at most nearly whole array store in stack at some point - 1