class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c):
            visited.add((r, c))

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != "1" or (nr, nc) in visited):
                    continue

                dfs(nr, nc)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands