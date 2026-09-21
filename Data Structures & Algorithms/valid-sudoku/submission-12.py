class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        rows_set = [set() for _ in range(len(board))]
        cols_set = [set() for _ in range(len(board))]
        box_set = [set() for _ in range(len(board))]

        for r in range(rows):
            for c in range(cols):
                box_row = r // 3
                box_col = c // 3
                box_index = box_row * 3 + box_col
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows_set[r]:
                    return False
                if board[r][c] in cols_set[c]:
                    return False
                if board[r][c] in box_set[box_index]:
                    return False
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                box_set[box_index].add(board[r][c])

        return True

        # Time complexity is O(N * M)
        # Space complexity is O(N) N rows N cols N boxes
                 