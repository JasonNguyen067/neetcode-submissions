class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                box_rows = r // 3
                box_cols = c // 3
                box_index = (box_rows * 3) + box_cols

                if value == ".":
                    continue

                if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
                
        return True

        # Time complexity O(M * N)
        # Space complexity O(M * N)


        