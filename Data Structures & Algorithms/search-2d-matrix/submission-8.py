class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        left = 0
        right = (cols * rows) - 1

        while left <= right:
            mid = (left + right) // 2
            col = (mid % cols)
            row = (mid // cols)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        # Time complexity O(M * N) for m rows n cols
        # Space complexity O(1) for the pointers