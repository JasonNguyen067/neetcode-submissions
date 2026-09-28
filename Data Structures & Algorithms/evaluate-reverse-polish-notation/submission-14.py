class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        Operators = ["+", "-", "/", "*"]

        for letter in tokens:
            if letter in Operators:
                right = stack.pop()
                left = stack.pop()

                if letter == "+":
                    stack.append(left + right)
                elif letter == "*":
                    stack.append(left * right)
                elif letter == "-":    
                    stack.append(left - right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(letter))
       
             # If its # 1 2 - left = 1 right = 2 we want 1 - 2 left - right

        return stack[-1]