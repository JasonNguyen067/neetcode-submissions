class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for val in tokens:
            if val in operators:
                right = stack.pop()
                left = stack.pop()

                if val == "+":
                    stack.append(left + right)
                elif val == "-":
                    stack.append(left - right)
                elif val == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(val))

        return stack[0]
