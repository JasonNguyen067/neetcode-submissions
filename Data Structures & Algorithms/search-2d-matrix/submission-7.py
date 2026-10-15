class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)

        left = 0
        right = (cols * rows) - 1

        while left <= right:
            mid = (left + right) // 2
            row = (mid // cols) # 5 divided by 3 rows is in row 1
            col = (mid % cols) # 5 modulus 4 is 1 so row 1 index 1

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False