class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box_row = r // 3 # Cuz if box_row 1 its supposed to be index 4
                box_col = c // 3 # Cuz if col is 3 its supposed to be 1 col to right
                box_index = (box_row * 3) + box_col

                if board[r][c] == ".":
                    continue

                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in boxes[box_index]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[box_index].add(board[r][c])

        return True
        