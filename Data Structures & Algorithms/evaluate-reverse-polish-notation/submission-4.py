class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operations = {"+", "-", "*", "/"}

        for value in tokens:
            if value in operations:
                right = int(stack.pop())
                left = int(stack.pop())
                if value == "+":
                    stack.append(left + right)
                elif value == "-":
                    stack.append(left - right)
                elif value == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(value))

        return stack[-1]

        