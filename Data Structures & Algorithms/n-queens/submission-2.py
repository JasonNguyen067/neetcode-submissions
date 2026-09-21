class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        backslash_diag = set()
        slash_diag = set()
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if (c in col or (r - c) in backslash_diag or(r + c) in slash_diag):
                    continue

                col.add(c)
                backslash_diag.add((r - c))
                slash_diag.add((r + c))
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                backslash_diag.remove((r - c))
                slash_diag.remove((r + c))
                board[r][c] = "."

        backtrack(0)
        return result