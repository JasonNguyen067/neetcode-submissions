class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack based solution
        # Pop when the current val is a operator and len(stack) is greater than or equal to 2
        # Will there ever be a case where len(stack) is greater than 2 when it gets appended?
        # Is stack assumed to have 1 val at the end 

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
        return stack[-1]

        # Time complexity is O(N) each val goes throuhg a add and pop operation
        # Space complexity is O(N) worst case stack is full
