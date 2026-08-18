class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        cols = len(matrix[0])
        rows = len(matrix)
        left = 0
        right = (cols * rows) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols 
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False