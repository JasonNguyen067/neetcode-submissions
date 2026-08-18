class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for value in tokens:
            if value in operations:
                right = stack.pop() #if you pop first top of stack gon be on right
                left = stack.pop()

                if value == "+":
                    stack.append(left + right)
                elif value == "-":
                    stack.append(left - right)
                elif value == "*":
                    stack.append(left * right)
                elif value == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(value))

        return stack[0]