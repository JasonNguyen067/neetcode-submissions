class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or 
                (r, c) in path or
                board[r][c] != word[i]
            ):
                return False

            path.add((r, c))


            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            path.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
        # Time Complexity O(M * 4^N) M being cell on board, 4 being choices on n levels
        # Space O(N)  recursion depth and path set can each contain at most N cells

        # Considered DFS but different of number of islands "technically backtrack aswell" cuz of the 
        # add and remove to paths