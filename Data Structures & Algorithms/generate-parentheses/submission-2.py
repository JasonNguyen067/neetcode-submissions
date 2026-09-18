class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(openCount, closeCount):
            if openCount == n and closeCount == n:
                result.append("".join(current))
                return

            if openCount < n:
                current.append("(")
                backtrack(openCount + 1, closeCount)
                current.pop()

            if closeCount < openCount:
                current.append(")")
                backtrack(openCount, closeCount + 1)
                current.pop()

        backtrack(0, 0)
        return result

        # Time complexity is 4^N 2^N * 2 
        # Space is O(N) N base case