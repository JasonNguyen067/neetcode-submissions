class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        best_island = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0

            visited.add((r, c))
            total = 1

            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)

            return total

        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                if area:
                    best_island = max(best_island, area)

        return best_island

        # Time complexity is O(M * N) M row N col 
        # Space complexity is O(M * N) worst case stores entire grid which it will and the call stack M * n worst case