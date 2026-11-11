class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combination = []

        def backtrack(openCount, closeCount):
            if openCount == n and closeCount == n:
                result.append("".join(combination))
                return

            if openCount < n:
                combination.append("(")
                backtrack(openCount + 1, closeCount)
                combination.pop()

            if closeCount < openCount:
                combination.append(")")
                backtrack(openCount, closeCount + 1)
                combination.pop()

        backtrack(0, 0)
        return result