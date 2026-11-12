class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combination = []

        def backTrack(openCount, closeCount):
            if openCount == n and closeCount == n:
                result.append("".join(combination))
                return

            if openCount < n:
                combination.append("(")
                backTrack(openCount + 1, closeCount)
                combination.pop()

            if closeCount < openCount:
                combination.append(")")
                backTrack(openCount, closeCount + 1)
                combination.pop()

        backTrack(0, 0)
        return result