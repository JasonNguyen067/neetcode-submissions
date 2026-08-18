class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operations = {"+", "-", "*", "/"}

        for value in tokens:
            if value in operations:
                right = stack.pop()
                left = stack.pop()
                if value == "+":
                    stack.append(left + right)
                elif value == "-":
                    stack.append(left - right)
                elif value == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right)) # Integer for float values
            else:
                stack.append(int(value)) # want to append as int because they are strings

        return stack[-1]